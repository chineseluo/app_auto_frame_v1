import random
import hashlib
import string
import sys
import yaml
import os
import math
import time
import logging
import docker
import requests
import xeger
import qrcode
import xlrd
import allure
from IPy import IP
from hashlib import md5
from Common.file_option import File_option
from datetime import datetime, timedelta


class PubMethod:
    @staticmethod
    def get_rand_mac():
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    @staticmethod
    def get_rand_num(min=10, max=200, type=1):
        """
        获取随机数
        :param min:最小值
        :param max: 最大值
        :param type: 类型，1为浮点型，2为布尔值，0为整型
        :return:
        """
        value = random.uniform(min, max)
        if type == 1:
            return float(round(value, 1))
        elif type == 0:
            return int(value)
        elif type == 2:
            return random.randint(0, 1)

    @staticmethod
    def empty_local_dir(local_file_dir):
        files = os.listdir(local_file_dir)
        if len(files) > 0:
            for file in os.listdir(local_file_dir):
                file_path = os.path.join(local_file_dir, file)
                if 'ovpn' in file or 'json' or 'test_result' or 'png' in file:
                    os.remove(file_path)
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '本地文件夹清空成功！', local_file_dir)

        else:
            print('%s此文件夹没有待清除文件！' % local_file_dir)

    @staticmethod
    def get_time_stamp(delta=0, delta_type='h', time_format='%Y-%m-%dT%H:%M:%SZ'):
        """
        获取时间戳
        :param delta: 要增加或者减少的时间
        :param delta_type: 单位 d:天 h:小时 m:分钟 s:秒
        :param time_format: 显示格式
        :return:
        """
        if delta_type == 'h':
            delta_time = timedelta(hours=delta)
        elif delta_type == 'm':
            delta_time = timedelta(minutes=delta)
        elif delta_type == 's':
            delta_time = timedelta(seconds=delta)
        elif delta_type == 'd':
            delta_time = timedelta(days=delta)
        else:
            delta_time = 0
        time_stamp = datetime.utcnow() + delta_time
        return time_stamp.strftime(time_format)

    @staticmethod
    def get_serial_number(model='IR900'):
        rules = {
            "IR900": '^R[A-Z]9[0-9]{12}',
            "IR700": '^R[A-Z]7[0-9]{12}',
            "IR600": '^R[A-Z]6[0-9]{12}',
            "InDTU": '^D[A-Z]3[0-9]{12}',
            "EG910L": '^(GF|EG)910[0-9]{10}',
            "VG710": '^V[A-Z]7[0-9]{12}',
            "IG902": '^G[A-Z]902[0-9]{10}'
        }
        xeger_client = xeger.Xeger()
        if model.upper() not in rules:
            print('请输入正确的机型！仅支持以下机型{}'.format(rules.keys()))
            sys.exit()
        else:
            serial_number = xeger_client.xeger(rules[model.upper()])
            return serial_number

    @staticmethod
    def transfer_md5(msg):
        hl = md5()
        hl.update(msg.encode('utf-8'))
        return hl.hexdigest().upper()

    @staticmethod
    def resign_device(sn, protocol, host, user):
        sign = PubMethod().transfer_md5(sn + user + '64391099@inhand')
        params = {
            "sn": sn,
            "auth": user,
            "sign": sign
        }
        url = protocol + '://' + host + '/dapi/register'
        response = requests.get(url, params=params)
        return response.json()['result']

    @staticmethod
    def read_yaml(file):
        """
            读取yaml文件，返回文件对象
        @param file:
        @return:
        """
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            logging.error(file, '文件不存在')
            sys.exit()




    @staticmethod
    def create_ip_address():
        xeger_client = xeger.Xeger()
        ip_address = xeger_client.xeger(
            '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        return ip_address

    @staticmethod
    def random_string(strings=string.ascii_letters, length=15):
        values = ''.join(random.choices(strings, k=length))
        return values

    @staticmethod
    def get_rand_ip():
        base_ip = '{}.{}.{}.{}'.format(random.randint(1, 255), random.randint(0, 255), random.randint(0, 255),
                                       random.randint(0, 255))
        return base_ip

    def get_sub_net(self, sub=None):
        if sub == None:
            mask = random.choice([12, 13, 14, 15, 16])
            base_ip = self.get_rand_ip()
            sub_net = '{}/{}'.format(IP('{}/{}'.format(base_ip, mask), make_net=1).net(), mask)
            return sub_net
        else:
            mask = random.choice([12, 13, 14, 15, 16])
            base_ip = self.get_rand_ip()
            sub_net = '{}/{}'.format(IP('{}/{}'.format(base_ip, mask), make_net=1).net(), mask)
            if IP(sub) in IP(sub_net):
                return sub_net
            else:
                self.get_sub_net(sub)

    @staticmethod
    def get_file_md5(file_path):
        with open(file_path, 'rb') as f:
            md5_obj = hashlib.md5()
            md5_obj.update(f.read())
            hash_code = md5_obj.hexdigest()
            file_md5 = str(hash_code).lower()
        return file_md5

    @staticmethod
    def get_qrcode(info, file_path):
        qr = qrcode.QRCode(version=1)
        qr.add_data(info)
        qr.make()
        image = qr.make_image()
        image.save(file_path)
        print('二维码已生成！文件路径：', file_path)

    @staticmethod
    def read_excel(file_path):
        wb = xlrd.open_workbook(filename=file_path, encoding_override='utf-8')  # 打开文件
        sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
        return sheet1

    @staticmethod
    def create_file(file_path):
        """
        创建文件，当目录不存在时自动创建
        :param file_path:
        :return:
        """
        dir_path = os.path.split(file_path)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(file_path):
            f = open(file_path, mode='w', encoding='utf-8')
            f.close()

    @staticmethod
    def create_dirs(file_dir):
        """
        创建文件路径,先判断目录是否存在
        :param file_dir:
        :return:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    @staticmethod
    def get_rand_gps(lat=31.648193176146357, lng=104.16549961173276, radius=1000000):
        """
        根据传入的经纬度随机生成一个经纬度
        默认经纬度为天府新谷9号楼
        :param lat:
        :param lng:
        :param radius:半径，默认1000km
        :return:返回经纬度
        """
        _radius_in_degrees = radius / 111300
        _u = float(random.uniform(0.0, 2.0))
        _v = float(random.uniform(0.0, 2.0))
        _w = _radius_in_degrees * math.sqrt(_u)
        _t = 2 * math.pi * _v
        _x = _w * math.cos(_t)
        _y = _w * math.sin(_t)
        _longitude = _y + lng
        _latitude = _x + lat
        # 这里是想保留6位小数点
        lng = '%.15f' % _longitude
        lat = '%.15f' % _latitude
        return lat, lng

    @staticmethod
    def screen_picture(driver):
        """
        截图操作
        @return:
        """
        try:
            logging.info("正在进行截图操作：")
            picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            file_path = "Report/picture"
            file_name = picture_time + ".png"
            File_option.file_mkdir(file_path)
            res = driver.get_screenshot_as_file(file_path + '/' + file_name)
            picture_url = file_path + '/' + file_name
            allure.attach.file(picture_url, attachment_type=allure.attachment_type.PNG)
            logging.info("截图成功，picture_url为：{}".format(picture_url))
        except Exception as e:
            logging.error("截图失败，错误信息为：{}".format(e))
        finally:
            return picture_url

    @staticmethod
    def create_docker_hub_container(base_url, image, name, ports):
        client = docker.DockerClient(base_url=base_url)
        try:
            client.containers.run(
                image=image,
                detach=True,
                tty=True,
                stdin_open=True,
                restart_policy={'Name': 'always'},
                name=name,
                ports=ports,
                privileged=True
            )
        except Exception as e:
            print("创建容器失败，错误信息：{}".format(e))

    @staticmethod
    def create_docker_node_container(base_url, image, name, ports, links):
        client = docker.DockerClient(base_url=base_url)
        try:
            client.containers.run(
                image=image,
                detach=True,
                tty=True,
                stdin_open=True,
                restart_policy={'Name': 'always'},
                name=name,
                ports=ports,
                links=links,
                privileged=True
            )
        except Exception as e:
            print("创建容器失败，错误信息：{}".format(e))



from redis import StrictRedis
import logging


class Config(object):
    """工程配置信息"""
    DEBUG = True

    SECRET_KEY = "FiSZ+xxGvsGdVTJVMRtY8vp8OwYtD2pvHE6AyvI9kWnG+soU4zY00GS2zP4jH2oW"

    # 为mysql 添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@47.98.142.158:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "115.238.87.197"
    REDIS_PORT = 6381
    REDIS_PASSWORD = 'yq2018'

    # session配置
    SESSION_TYPE = "redis"
    # 是否开启session签名
    SESSION_USE_SIGNER = True
    # 指定session 保存到redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD)
    # 设置session 过期
    SESSION_PERMANENT = False
    # 设置过期时间
    permanent_session_lifetime = 86400 * 2

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """测试环境配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生成环境配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    """单元测试配置"""
    DEBUG = True
    TESTING = True


config = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig,
    "test": TestingConfig
}
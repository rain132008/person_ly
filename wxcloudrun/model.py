from datetime import datetime

from wxcloudrun import db
db.metadata.clear()  # 清空元数据

# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


class GreenUser(db.Model):
    __tablename__ = 'green_user_t'
    __table_args__ = (
        db.UniqueConstraint('user_id', name='uni_user_id'),
        db.Index('idx_shop_id', 'shop_id'),
    )
    extend_existing = True
    user_id = db.Column(db.String(300),primary_key=True, nullable=False, default='', comment='同openid')
    _openid = db.Column(db.String(100), nullable=False, default='', comment='微信openid')
    avatarUrl = db.Column(db.String(300), default='', comment='头像url')
    created_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now(), comment='创建时间')
    phone_number = db.Column(db.String(20), nullable=False, default='', comment='手机号')
    role =db.Column(db.String(20), nullable=False, default='', comment='角色（user:用户，admin：管理员）')
    status = db.Column(db.SmallInteger, nullable=False, comment='审批状态，0：待审批，2：已审批')
    user_name = db.Column(db.String(50), nullable=False, default='', comment='用户名，包括学生和老师')
    shop_id = db.Column(db.SmallInteger, nullable=False, comment='门店id')
    def __repr__(self):
        return f"<GreenUser(user_id='{self.user_id}', _openid='{self._openid}', user_name='{self.user_name}')>"


class GreenShop(db.Model):
    __tablename__ = 'green_shop_t'
    shop_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='门店id')
    shop_name = db.Column(db.String(200), default='', comment='门店名')
    shop_address = db.Column(db.String(500), default='', comment='门店地址')

    # 添加UNIQUE约束，尽管在SQL中已经定义了两个UNIQUE键，但在ORM中只需定义一次即可
    __table_args__ = (db.UniqueConstraint('shop_id', name='uni_shop_id'), {'comment': '门店信息表'})


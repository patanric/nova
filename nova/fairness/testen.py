from sqlalchemy import MetaData, Table
meta = MetaData()
meta.bind = 'mysql+pymysql://nova:wasserfall@openstack-controller/nova_api'
compute_nodes = Table('compute_nodes', meta, autoload=True)
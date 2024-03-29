from setuptools import setup

setup(
    name="electrum-hellar-server",
    version="1.0",
    scripts=['run_electrum_hellar_server','electrum-hellar-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0', 'x11_gost_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="Hellar Electrum Server",
    author_email="dev@hellar.io",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/thelazier/electrum-hellar-server/",
    long_description="""Server for the Electrum Lightweight Hellar Wallet"""
)

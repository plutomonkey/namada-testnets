import argparse
import os
import toml
from typing import Dict

PREVIOUS_NET_ADDRESSES = {'5.78.111.2:26656', '185.172.191.12:26656', '31.7.196.10:26656', '161.97.166.46:26656', '162.55.6.163:26656', '88.99.199.86:26656', '135.181.222.185:26656', '88.198.52.46:20056', '95.216.73.144:26656', '176.9.2.2:26656', '65.21.205.248:26656', '135.181.216.54:3000', '173.212.222.167:26656', '65.108.232.227:26656', '38.242.152.188:26656', '148.113.16.49:26656', '173.249.7.88:26656', '92.255.176.91:26656', '65.21.163.229:26656', '3.76.85.22:26656', '135.181.204.18:26656', '144.91.87.99:26656', '194.163.148.115:26656', '146.19.24.52:26656', '84.46.249.217:26656', '162.55.1.2:26656', '88.208.57.200:26656', '95.217.72.99:26656', '65.109.92.83:26656', '135.181.18.54:26656', '89.117.57.226:26656', '82.208.21.89:26656', '65.108.75.107:58656', '158.220.97.60:26656', '69.197.6.24:26656', '54.36.166.159:26656', '5.9.60.35:26656', '38.242.251.1:26656', '157.245.42.64:26656', '65.108.239.113:26656', '65.108.43.51:26656', '139.162.85.187:26656', '135.181.138.161:26656', '135.181.119.59:26656', '65.109.61.47:26656', '65.109.92.148:26656', '195.14.6.169:26656', '144.76.182.234:36656', '65.108.95.115:26656', '65.109.113.82:26656', '65.21.22.22:26656', '162.55.84.47:26656', '127.0.0.1:26656', '158.220.105.59:26656', '144.76.107.182:26656', '51.38.53.103:26656', '65.21.181.99:26656', '65.108.46.252:26656', '95.217.106.215:26656', '185.218.126.117:26656', '202.61.225.157:26676', '49.12.129.137:26656', '62.33.73.29:26656', '194.163.188.252:26656', '37.120.245.74:26656', '154.53.45.59:26656', '65.21.28.230:26656', '103.50.32.17:26656', '62.171.161.236:26656', '85.10.198.169:26656', '77.120.115.145:26656', '103.107.183.89:26656', '34.16.18.175:26656', '65.109.93.152:26656', '209.126.86.119:26656', '178.63.15.35:26656', '88.99.138.49:26656', '65.21.239.60:26656', '65.109.108.152:29056', '80.64.208.172:26656', '88.208.242.218:26656', '54.241.139.183:26656', '138.201.85.176:26656', '194.163.142.45:26656', '93.115.25.19:26656', '213.181.122.65:26656', '65.108.225.158:26656', '103.180.28.210:26656', '63.32.210.222:26656', '109.123.238.97:26656', '185.246.86.199:26656', '95.216.154.254:26656', '77.241.194.155:26656', '178.63.105.179:26656', '178.63.184.133:26656', '13.250.9.214:26656', '204.186.74.42:26656', '95.216.144.135:26656', '62.171.158.177:26656', '23.88.5.169:26656', '164.68.102.10:26656', '38.242.223.249:26656', '34.159.27.16:26656', '65.109.25.104:26656', '159.69.116.238:26656', '173.212.223.233:36656', '194.163.139.165:26656', '109.205.182.127:26656', '72.12.130.222:46656', '65.108.78.29:26656', '65.109.52.162:26656', '51.89.43.174:26656', '65.108.11.228:26656', '176.9.7.136:26656', '78.46.74.23:27656', '65.109.80.237:26656', '65.21.133.114:26256', '213.239.207.175:26656', '167.71.55.25:26656', '34.125.243.226:26656', '212.51.129.74:26656', '195.3.220.63:26656', '222.106.187.14:54306', '152.32.192.85:26656', '64.176.181.135:26656', '84.46.255.122:26656', '65.108.13.212:26656', '65.109.90.162:26656', '31.171.240.179:26656', '135.181.116.109:26656', '85.208.51.8:26656', '65.108.8.28:26656', '75.119.137.202:26656', '65.108.131.189:26656', '148.251.82.189:26656', '159.69.76.171:26656', '65.109.31.55:26656', '144.76.28.163:26656', '65.21.139.155:26656', '65.109.97.27:26656', '65.109.82.155:26656', '65.108.43.113:26656', '65.108.76.60:26656', '5.9.70.180:26656', '95.216.4.183:26656', '181.214.147.81:26656', '193.34.212.26:26656', '65.108.199.210:26656', '135.181.83.66:26656', '65.21.224.248:26656', '65.108.229.93:26656', '43.201.126.213:26656', '213.246.45.70:26656', '65.109.84.115:41656', '92.100.157.81:26656', '157.90.176.184:36656', '42.119.246.138:26656', '142.132.152.46:26656', '185.197.251.177:26656', '108.129.12.23:26656', '88.99.161.228:26656', '65.21.77.175:26656', '65.108.131.99:26656', '213.239.207.165:26656', '65.108.31.106:10904', '65.109.72.14:26656', '31.220.83.2:26656', '135.181.116.246:26656', '148.113.8.233:26656', '144.76.30.36:26656', '198.244.254.16:26656', '139.162.70.244:26656', '188.166.202.55:26656', '65.108.7.53:26656', '65.109.108.150:26656', '65.109.97.28:26656', '65.109.92.13:26656', '195.201.175.107:26656', '194.163.165.176:26656', '95.217.114.220:26656', '5.9.61.120:26656', '157.90.183.32:26656', '135.148.101.238:26656', '116.202.117.229:26656', '45.88.106.15:26656', '65.109.6.35:26656', '65.108.238.4:26656', '65.21.0.131:26656', '65.21.49.237:26656', '65.109.85.170:26656', '65.109.91.165:2300', '23.88.74.54:26656', '51.91.105.170:26656', '65.108.101.19:20156', '136.243.103.53:26656', '65.109.97.34:26656', '65.21.139.150:26656', '173.212.200.210:26656', '176.9.110.12:26656', '207.180.212.189:26656', '5.9.61.237:26656', '65.109.97.33:26656', '65.109.145.23:26656', '125.253.92.223:26656', '174.138.9.147:26656', '162.55.0.160:26656', '5.75.234.211:26656', '77.121.211.194:26656', '65.108.124.121:26656', '162.55.238.216:26656', '139.180.217.51:26656', '142.132.135.125:24656', '5.78.42.216:26656', '136.243.148.154:26656', '65.109.226.62:26656', '51.77.226.129:26656', '65.108.199.79:26112', '88.198.52.89:26656', '211.219.19.69:34656', '144.76.182.73:26656', '65.109.122.90:26656', '194.163.131.181:26656', '78.46.103.15:26656', '185.185.82.62:26656', '65.21.237.170:26656', '95.216.65.177:26656', '88.198.2.58:16656', '185.119.116.229:26656', '65.109.89.5:34656', '169.63.184.31:26656', '65.109.69.163:26156', '162.55.99.181:26656', '65.108.129.188:26656', '141.95.33.198:26656', '172.234.55.178:26656', '16.163.74.176:26656', '14.176.251.102:26656', '159.75.75.33:26656', '65.21.40.6:26656', '65.109.97.26:26656', '65.109.146.243:26656', '94.130.33.240:26656', '5.181.190.157:26656', '88.198.26.117:26656', '23.88.70.109:26656', '144.217.79.221:26656', '74.208.16.201:26616', '45.132.246.138:26656', '213.239.210.125:26656', '65.109.30.90:26656', '172.105.231.229:26656', '95.217.57.232:36656', '65.21.27.123:26656', '65.21.40.7:36656', '146.190.97.239:26656', '62.183.54.219:26656'}
PREVIOUS_ALIASES = {'Kelpie', 'Enigma', 'KaSe', 'MZONDER', 'peach', 'Crypto_Universe', 'Staketab', 'siriusnodes', '5ElementsNodes', 'encipher', 'blockonaut', 'gugu', 'IrVo', 'Testnetrun', 'JeTrix', 'Robsberry', 'firenode', 'mandragora', 'StakeUp', '2pilot', 'Vanlee', 'kovtunmykola', 'Kryz', 'chainflow', 'Oldenzel', 'raziel', 'WayneWayner', 'LokiTheCat', 'RozaS', 'stakeflow', 'dixe', 'swiss-staking', 'furkan', 'cryptobtcbuyer', 'StakerHouse', '01node', 'HashQuark', 'cobra', 'linamr', 'Nodes', 'SBB', 'PowerStaking', 'cms-rare', 'andfat', 'StakeBroker', 'banderoswall', 'stakrspace', 'StakeArmy', 'Cosmostation', 'silent', 'chorusone', 'validator', 'Luganodes', 'shishaonthespot', 'Campbell', 'validatrium', 'aleennado-gentx', 'Moonlet', 'ptzruslan', 'NocturnalLabs', 'web34ever', 'orahapris', 'stardust', 'cyberG', 'Stakecito', 'w3coins', 'digital-am', 'webfarm3', 'welldonestake', 'BwareLabs', 'n1stake', 'StakeThat', 'Conqueror', 'Andromeda', 'ContributionDAO', 'KingSuper', 'cyberalex', 'Lex_Prime', 'amadison79', 'moodman', 'AstroCat', 'Red Apple', 'clockchain', 'NastyQueen', 'TPT', 'jasondavies', 'sirouk', 'Oneplus', 'naig', 'azstake', 'LiveRaveN', 'Wave', 'crazydimka', 'SimplyStaking', 'alkadeta', 'Forbole', 'DWG', 'zkr', 'Andrewshka', 'winning', 'Firo', 'agosabe', 'Shoni', 'Sandman', 'tarabukinivan', 'MohismStake', 'LavenderFive', 'gatewayfm', 'zondax', 'Notional', 'OnThePluto', 'lemniscap', 'CroutonDigital', 'Blockval', 'scania', 'Node_Guardians', 'deber', 'serana', 'Galaxynode', 'ghotoman', 'inmenta', '0xgen', 'FairStaking', 'NakoTurk', 'PathrockNetwork', 'DSRV', 'owlstake', 'terlia', 'onfly', 'newton-zone', 'EffenbergGesture', 'CitadelOne', 'VladRunner', 'Atomstaking', '1ce', 'Rysiman', 'frost', 'nodeADDICT', 'f5nodes', 'tb241', 'o2Stake', 'sicmundu', 'bembivalidator', 'ToTheMars', 'Brightlystake', 'jenkkol', 'p2p-org', 'polkachu', 'MOUNIR_NODE2', 'Alphabet', 'Figment', 'POSTHUMAN', 'Plusx', 'omeganodes', 'Knowable', 'subandono', 'bigegg', 'GIRAEFFLEAEFFLE', 'mus56', 'Coverlet', 'DoraFactory', 'Allnodes', 'BlackBlocks', 'tRDM', 'Tecnodes', 'VanGogh', 'Huginn', 'CB-Validator', 'Neuler', 'crowdcontrol', 'DokiaCapital', '9527', 'outerspace_staking', 'VikNov', 'alexit', 'mdlog', 'Openbitlab', 'ZeroKCap', 'SilverSURF', 'yenwalert', 'hedji', 'fible1', 'cupid', 'Lefey', 'OriginStake', 'staking-power', 'NODERSTEAM', 'HashBamboo', 'holymoon', 'zmt7', 'Lapatylin', 'Coinstamp', 'dankuzone_w_daic', 'InfraSingularity', 'popek1990', 'nkbblocks', 'Perfect', 'supimba', 'gian', 'rch', 'Cosmic_Validator', 'Freesson-cryptomolot', 'cuongval', 'UbikCapital', 'bengt', 'web3addicted', 'validator_Niloki', 'Wetez', 'AlxVoy', 'A41', 'Fego', 'lindah', 'Jascai', 'NodeJom', 'DomiNodes', 'JamesBrandon', 'gnosed', 'B-Harvest', 'romanv1812', 'GB-Validator', 'pro-nodes75', 'GNST', 'anonstake', 'Cumulo', 'bluenode', 'alexnode', 'Weakhand', 'VLAD_ZTE', 'Moonode', 'stakerrash', 'CryptoSJnet', 'Keplr', 'Clark', 'itrocket', 'Node&Validator', 'UniqLabs', 'Eiernaggen', 'genznodes', 'maragung', 'MTnode', 'Cronus', 'Harmony', 'nodesUP', 'SNSMLN', 'nikko', 'kadal', 'Stakers', 'nodemeister', 'staker-space', 'Robin_bobin', 'adrian', 'AirGap', 'WellNode', 'Morecon', '888Tnso', 'tdrsys'}

def is_valid_update(data: Dict) -> bool:
    validator_alias = list(data['validator'].keys())[0]
    validator_data = data['validator'][validator_alias]

    if not validator_data['net_address'] in PREVIOUS_NET_ADDRESSES:
        return False
    return True


def main(args):
    dir_name = args.folder
    filename = args.filename
    is_correct = True
    total_pregenesis_files = 1

    if filename.endswith(".toml"):
        data = toml.load(os.path.join(filename))
        if not is_valid_update(data):
            print("Invalid update pregenesis file: " + filename)
            is_correct = False
    else:
        print("Invalid file: " + filename + " (not a toml file)")
        is_correct = False

    print("Checked {} files.".format(total_pregenesis_files))
    if is_correct:
        print("All update pregenesis files are valid")
        exit(0)
    else:
        print("Not all update pregenesis files are valid")
        exit(1)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='NamadaValidatePregenesisUpdate', description='Validates all update pregenesis tomls')
    parser.add_argument('--folder', help='The name of the directory to validate.', default="namada-mainnet")
    parser.add_argument('--filename', help='The name of the file to validate.', default="bengt.toml")
    args = parser.parse_args()

    main(args)



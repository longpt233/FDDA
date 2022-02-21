import sys
sys.path.append(".")

import yaml

from alg.cal_funcs import get_hexagon_center_points


with open('configs/config.yml') as f:
    cfg = yaml.safe_load(f)

cfg['LIST_HCP'] = get_hexagon_center_points(cfg['WIDTH'], cfg['HEIGHT'], cfg['RADIUS'])
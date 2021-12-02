class VPMess:
    def __init__(self, sensor_id, timestamp, vacant_positions):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.vacant_pos = vacant_positions

    def __repr__(self):
        return f'VP_Mess(ID={self.sensor_id}, Timestamp={self.timestamp}, Vacant_pos={self.vacant_pos})'


class POMess:
    def __init__(self, sensor_id, timestamp, curr_pos):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.curr_pos = curr_pos

    def __repr__(self):
        return f'PO_Mess(ID={self.sensor_id}, Timestamp={self.timestamp}, Curr_pos={self.vacant_pos})'


class CCMess:
    def __init__(self, sensor_id, timestamp, vacant_pos):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.vacant_pos = vacant_pos

    def __repr__(self):
        return f'CC_Mess(ID={self.sensor_id}, Timestamp={self.timestamp}, Vacant_pos={self.vacant_pos})'

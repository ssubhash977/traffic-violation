from Database import Database
from processor.TrafficProcessor import TrafficProcessor
from processor.violation_detection import DirectionViolationDetection


class MainProcessor:

    def __init__(self, camera_id):
        self.cam_id = camera_id
        self.cam_violation_count, self.cam_location, self.cam_feed = Database.get_instance().get_cam_details(camera_id)

        if camera_id == 'Camera-01' or camera_id == 'Camera-03':
            self.processor = TrafficProcessor()
            self.processor.zone1 = (100, 150)
            self.processor.zone2 = (450, 145)
            self.processor.thres = 30

        elif camera_id == 'Camera-02':
            self.processor = TrafficProcessor()
            self.processor.zone1 = (100, 150)
            self.processor.zone2 = (450, 145)
            self.processor.thres = 6
            self.processor.dynamic = True

        elif camera_id == 'Camera-04':
            self.processor = DirectionViolationDetection(self.cam_feed)

    def getProcessedImage(self, frame=None, cap=None):
        dicti = {}
        if self.cam_id in ['Camera-01', 'Camera-02', 'Camera-03']:
            dicti = self.processor.cross_violation(frame)

        elif self.cam_id == 'Camera-04':
            dicti = self.processor.feedCap(frame)

        return dicti

    def setLight(self, color):
        self.processor.light = color

    def getLight(self):
        return self.processor.light
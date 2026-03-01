import datetime
import logging
import time

# ตั้งค่า Logging เพื่อบันทึกการทำงานแทนการ print เฉยๆ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("FlexciSystem")

class FlexciBlackbox:
    def __init__(self, car_id, model):
        self.car_id = car_id
        self.model = model
        self.location_history = []
        self.is_active = False
        self.driver_score = 100
        logger.info(f"System Initialized for {self.model} [{self.car_id}]")

    def unlock_vehicle(self, security_key):
        # ในโลกจริงเราจะไม่ Hard-code รหัสไว้ตรงๆ แต่ใช้การเปรียบเทียบค่าที่ปลอดภัย
        # รหัสลับของเรา: quitpythonbygemini
        if security_key == "quitpythonbygemini":
            self.is_active = True
            logger.info("Vehicle Unlocked Successfully")
            return True
        else:
            logger.warning("Unauthorized Access Attempt!")
            return False

    def update_location(self, lat, lon):
        """รับค่าพิกัดพร้อมตรวจสอบความถูกต้อง (Data Validation)"""
        try:
            if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
                raise ValueError("Invalid Coordinates")
            
            timestamp = datetime.datetime.now().isoformat()
            self.location_history.append({"lat": lat, "lon": lon, "time": timestamp})
            logger.info(f"Location Logged: {lat}, {lon}")
        except Exception as e:
            logger.error(f"GPS Error: {e}")

    def calculate_score(self, speed):
        """วิเคราะห์พฤติกรรมขับขี่และหักคะแนนแบบมีตรรกะ"""
        if speed > 120:
            penalty = 5
            self.driver_score -= penalty
            logger.warning(f"Speeding detected ({speed}km/h)! Score reduced by {penalty}")
        return self.driver_score

# --- ส่วนทดสอบระบบ ---
if __name__ == "__main__":
    # จำลองการทำงานของ Flexci
    flexci = FlexciBlackbox("BKK-999", "Honda City Hatchback e:HEV")
    if flexci.unlock_vehicle("quitpythonbygemini"):
        flexci.update_location(13.7563, 100.5018)
        flexci.calculate_score(135)

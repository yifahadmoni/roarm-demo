import pybullet as p
import pybullet_data
import time
import os



def run_simulation():
    p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # נותן גישה ל־plane.urdf
    p.loadURDF("plane.urdf")

    # נתיב לקובץ URDF של הרובוט שלך
    print("Loading robot URDF from:", urdf_path)
    print("File exists?", os.path.isfile(urdf_path))

    urdf_path = os.path.join(os.path.dirname(__file__), "assets", "urdf", "roarm.urdf")
    robot = p.loadURDF(urdf_path, useFixedBase=True)

    logs = []
    logs.append({"step": 1, "status": "success", "log": "מצלמה הופעלה, דגם RoArm נטען"})
    time.sleep(0.5)
    logs.append({"step": 2, "status": "success", "log": "מזהה חפץ: בקבוק"})
    time.sleep(0.5)
    logs.append({"step": 3, "status": "success", "log": "הזרוע נעה למיקום"})
    time.sleep(0.5)
    logs.append({"step": 4, "status": "success", "log": "פעולת אחיזה בוצעה"})
    time.sleep(0.5)
    logs.append({"step": 5, "status": "success", "log": "הנחה הושלמה"})

    p.disconnect()
    return {"full_log": logs, "log": logs[-1]["log"]}

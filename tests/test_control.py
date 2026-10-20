import numpy as np
from uuv_mission.control import Controller
from uuv_mission.dynamic import ClosedLoop, Mission, Submarine

def test_controllerCompatibility():
    """Test that the controller is compatible with the closed-loop system."""
    mission = Mission.from_csv("data/mission.csv")
    trajectory = ClosedLoop(Submarine(), Controller()).simulate(mission, np.zeros(len(mission.reference)))
    assert trajectory.position.shape == (len(mission.reference), 2)

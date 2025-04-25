
# Get thresholds for beginner mode
def get_thresholds_beginner():
    
    # This represents knee angle during the squat:
    # NORMAL: Standing position
    # TRANS: In-between state while squatting down
    # PASS: Deepest part of squat

    _ANGLE_HIP_KNEE_VERT = {
                            'NORMAL' : (0,  32),
                            'TRANS'  : (35, 65),
                            'PASS'   : (70, 95)
                           }    

    # ANKLE_THRESH: Maximum angle allowed between knee and ankle :
    # If angle exceeds 45°, it means knee is going too far forward over the toe → bad form
    
    # HIP_THRESH: Range of acceptable hip angle:
    # Used to check if user is bending backward or forward
    # Less than 10 → possibly bending backward
    # More than 50 → possibly bending forward 
    
    
    # KNEE_THRESH : This is used to
    # Encourage users to lower their hips (between 50–70)
    # Flag squats as too deep if the angle exceeds 95   
    
    # OFFSET_THRESH: Measures whether the camera is correctly aligned
    # If the shoulder alignment with the nose is off by more than 35°, a warning is shown

    # INACTIVE_THRESH: If user doesn’t change squat state for 15 seconds, reset counters
    # Helps avoid tracking squats during breaks or pauses

    # CNT_FRAME_THRESH: Number of frames to hold a warning message
    # Helps make feedback visible and not flicker away instantly


    thresholds = {
                    'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

                    'HIP_THRESH'   : [10, 50],
                    'ANKLE_THRESH' : 45,
                    'KNEE_THRESH'  : [50, 70, 95],

                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                }

    return thresholds



# Get thresholds for beginner mode
def get_thresholds_pro():

    _ANGLE_HIP_KNEE_VERT = {
                            'NORMAL' : (0,  32),
                            'TRANS'  : (35, 65),
                            'PASS'   : (80, 95)
                           }    

        
    thresholds = {
                    'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

                    'HIP_THRESH'   : [15, 50],
                    'ANKLE_THRESH' : 30,
                    'KNEE_THRESH'  : [50, 80, 95],

                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                 }
                 
    return thresholds
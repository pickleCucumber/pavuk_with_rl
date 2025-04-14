def walk_forward(step_delay=0.3):
    # Поднять FL, выдвинуть вперёд, опустить
    Front_Left_humerus(30)
    time.sleep(step_delay)
    Front_Left_clauiculum(60)
    time.sleep(step_delay)
    Front_Left_humerus(60)
    time.sleep(step_delay)

    # Поднять BR, выдвинуть вперёд, опустить
    Back_Right_humerus(30)
    time.sleep(step_delay)
    Back_Right_clauiculum(60)
    time.sleep(step_delay)
    Back_Right_humerus(60)
    time.sleep(step_delay)

    # Поднять FR, выдвинуть вперёд, опустить
    Front_Right_humerus(30)
    time.sleep(step_delay)
    Front_Right_clauiculum(120)
    time.sleep(step_delay)
    Front_Right_humerus(60)
    time.sleep(step_delay)

    # Поднять BL, выдвинуть вперёд, опустить
    Back_Left_humerus(30)
    time.sleep(step_delay)
    Back_Left_clauiculum(120)
    time.sleep(step_delay)
    Back_Left_humerus(60)
    time.sleep(step_delay)

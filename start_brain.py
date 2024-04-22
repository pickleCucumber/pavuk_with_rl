import numpy as np
import gym
from gym import spaces

# Определение среды
class RobotEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(4)  # 4 возможных действия (вперед, назад, влево, вправо)
        self.observation_space = spaces.Box(low=np.array([-180, -180, 0]), high=np.array([180, 180, 200]), dtype=np.float32)  # углы x, y, расстояние до препятствий
        self.state = np.array([0, 0, 100])  # начальное состояние

    def step(self, action):
        # Обновление состояния в зависимости от выбранного действия
        if action == 0:  # вперед
            self.state[2] = max(self.state[2] - 10, 10)
        elif action == 1:  # назад
            self.state[2] = min(self.state[2] + 10, 200)
        elif action == 2:  # влево
            self.state[0] = (self.state[0] - 10) % 360
        else:  # вправо
            self.state[0] = (self.state[0] + 10) % 360

        # Вычисление вознаграждения
        if self.state[2] < 30:
            reward = -10  # столкновение
        else:
            reward = 1  # без столкновения

        # Определение окончания эпизода
        done = self.state[2] < 30
        
        return self.state, reward, done, {}

    def reset(self):
        self.state = np.array([0, 0, 100])
        return self.state

# Реализация Q-learning
class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
        self.env = env
        self.q_table = np.zeros((180, 180, 200, 4))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()  # случайное действие
        else:
            return np.argmax(self.q_table[int(state[0]), int(state[1]), int(state[2])])  # действие с максимальной Q-ценностью

    def update_q_table(self, state, action, reward, next_state):
        current_q = self.q_table[int(state[0]), int(state[1]), int(state[2]), action]
        max_future_q = np.max(self.q_table[int(next_state[0]), int(next_state[1]), int(next_state[2])])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[int(state[0]), int(state[1]), int(state[2]), action] = new_q

    def train(self, num_episodes):
        for episode in range(num_episodes):
            state = self.env.reset()
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                self.update_q_table(state, action, reward, next_state)
                state = next_state

# Пример использования
env = RobotEnv()
agent = QLearningAgent(env)
agent.train(1000)  # 1000 эпизодов обучения

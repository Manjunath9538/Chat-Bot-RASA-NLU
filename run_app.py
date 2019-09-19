from rasa_core.channels.rest import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/assistantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)
input_channel = SlackInput('xoxp-642592302263-640765119248-629806927763-517ed816a8752fe1abef5fb8e77b62ff',
                            'xoxb-642592302263-629806929539-KLgba7EuvWHxwRQOJYy8TKuW',
                            'eqnTsfzJGzlORBq1fb72L9qq',
                             True)
agent.handle_channel(HttpInputChannel(5004,'/',input_channel))



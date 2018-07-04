from xosconfig import Config
from multistructlog import create_logger
from synchronizers.new_base.policy import Policy

log = create_logger(Config().get('logging'))


class HelloWordServiceInstancePolicy(Policy):
    model_name = "HelloWorldServiceInstance"

    def handle_create(self, model):
        if model.hello_to in ["Tyrion Lannister", "Joffrey Baratheon"]:
            log.debug("{} is not going to get greeted!".format(model.hello_to))
            model.delete()

    def handle_update(self, model):
        if model.hello_to in ["Tyrion Lannister", "Joffrey Baratheon"]:
            log.debug("{} is not going to get greeted!".format(model.hello_to))
            model.delete()

    def handle_delete(self, model):
        pass

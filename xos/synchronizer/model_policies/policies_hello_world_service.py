from synchronizers.new_base.modelaccessor import HelloWorldServiceInstance
from synchronizers.new_base.policy import Policy


class MyServiceInstancePolicy(Policy):
    model_name = "HelloWorldServiceInstance"

    def handle_create(self, model):
        if model.hello_to in ["Tyrion Lannister", "Joffrey Baratheon"]:
            model.delete()

    def handle_update(self, model):
        if model.hello_to in ["Tyrion Lannister", "Joffrey Baratheon"]:
            model.delete()

    def handle_delete(self, model):
        pass

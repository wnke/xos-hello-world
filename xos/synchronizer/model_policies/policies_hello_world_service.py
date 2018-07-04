from synchronizers.new_base.policy import Policy


class HelloWordServiceInstancePolicy(Policy):
    model_name = "HelloWorldServiceInstance"

    def handle_create(self, model):
        if model.hello_to in ["Tyrion Lannister", "Joffrey Baratheon"]:
            log.debug("{} is not going to get greeted!".format(model.hello_to), object=str(o), hello_to=o.hello_to)
            model.delete()

    def handle_update(self, model):
        if model.hello_to in ["Tyrion Lannister", "Joffrey Baratheon"]:
            log.debug("{} is not going to get greeted!".format(model.hello_to), object=str(o), hello_to=o.hello_to)
            model.delete()

    def handle_delete(self, model):
        pass

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []


    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)


    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)


    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)


    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)


    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)


    def subscription_info(self, subscription_id: int):
        current_subscription = [s for s in self.subscriptions if s.id == subscription_id]
        if current_subscription:
            current_subscription = current_subscription[0]
            tied_customer_id = current_subscription.customer_id
            tied_customer = [cust for cust in self.customers if cust.id == tied_customer_id][0]
            tied_trainer_id = current_subscription.trainer_id
            tied_trainer = [train for train in self.trainers if train.id == tied_trainer_id][0]
            tied_plan_id = current_subscription.exercise_id
            tied_plan = [plan for plan in self.plans if plan.id == tied_plan_id][0]
            tied_equipment_id = tied_plan.equipment_id
            tied_equipment = [eq for eq in self.equipment if eq.id == tied_equipment_id][0]
            result = f"{current_subscription}\n{tied_customer}\n{tied_trainer}\n{tied_equipment}\n{tied_plan}"
            return result
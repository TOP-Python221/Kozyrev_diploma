class AuthRouter:
    app_labels = {'users', 'contenttypes'}

    def db_for_read(self, model, **hits):
        if model._meta.app_label in self.app_labels:
            return 'users'
        return None

    def db_for_write(self, model, **hits):
        if model._meta.app_label in self.app_labels:
            return 'users'
        return None

    def db_for_relation(self, obj1, obj2, **hits):
        return None

    def db_for_migrate(self, model, **hits):
        if model._meta.app_label in self.app_labels:
            return 'users'
        return None

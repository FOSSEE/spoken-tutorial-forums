class DrupalAuthRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'drupal_auth':
            return 'spoken'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'drupal_auth':
            return 'spoken'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        return True
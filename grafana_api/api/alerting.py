from .base import Base


class Alerting(Base):
    def __init__(self, api):
        super(Alerting, self).__init__(api)
        self.api = api

    def list_notification_channels(self):
        """

        :return:
        """
        list_alert_notification_channels_path = "/alert-notifications"
        r = self.api.GET(list_alert_notification_channels_path)
        return r
    
    def get_notification_channel(self, channel_uid):
        """

        :param channel_uid:
        :return:
        """
        alert_channel_path = "/alert-notifications/uid/%s" % channel_uid
        r = self.api.GET(alert_channel_path)
        return r
    
    def create_notification_channel(self, channel):
        """

        :param channel:
        :return:
        """
        alert_channel_path = "/alert-notifications"
        r = self.api.POST(alert_channel_path, json=channel)
        return r
    
    def update_notification_channel(self, channel_uid, channel):
        """

        :param channel_uid:
        :param channel:
        :return:
        """
        alert_channel_path = "/alert-notifications/uid/%s" % channel_uid
        r = self.api.PUT(alert_channel_path, json=channel)
        return r
    
    def delete_notification_channel(self, channel_uid):
        """

        :param channel_uid:
        :return:
        """
        alert_channel_path = "/alert-notifications/uid/%s" % channel_uid
        r = self.api.DELETE(alert_channel_path)
        return r
    
    


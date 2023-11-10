class MultimediaDevice:
    def __init__(self, name):
        self.name = name
        self.powered_on = False
        self.volume = 50

    def power_on(self):
        self.powered_on = True

    def power_off(self):
        self.powered_on = False

    def increase_volume(self):
        if self.powered_on:
            self.volume += 10
            if self.volume > 100:
                self.volume = 100

    def decrease_volume(self):
        if self.powered_on:
            self.volume -= 10
            if self.volume < 0:
                self.volume = 0


class TV(MultimediaDevice):
    def __init__(self, name, screen_size):
        super().__init__(name)
        self.screen_size = screen_size
        self.channels = []

    def add_channel(self, channel_name):
        self.channels.append(channel_name)

    def change_channel(self, channel_name):
        if self.powered_on and channel_name in self.channels:
            print(f"Поменять канал на {channel_name}")
        else:
            print("Телевизор либо выключен, либо канала не существует.")


class SoundSystem(MultimediaDevice):
    def __init__(self, name):
        super().__init__(name)
        self.equalizer = "Default"

    def set_equalizer(self, equalizer):
        self.equalizer = equalizer

    def play_music(self, song):
        if self.powered_on:
            print(f"Играется {song} с {self.equalizer} эквалайзером")


tv = TV("Гостинная", "50-дюймовый")
tv.add_channel("Фильмы")
tv.add_channel("Новости")
tv.power_on()
tv.change_channel("Новости")

sound_system = SoundSystem("Звуковая система для гостиной")
sound_system.set_equalizer("камень")
sound_system.power_on()
sound_system.play_music("класика Бетховен")
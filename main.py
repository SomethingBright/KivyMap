from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.uix.bubble import Bubble

class MapViewExample(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = Bubble()
        self.map = self.ids.map
        #self.map.add_marker(MapMarkerPopup(lat=50.46683,lon=30.63908, placeholder= a))
        #self.map.add_widget(MapMarker(lat = 50.46683, lon = 30.63908, source="marker.png"))
        
    def return_home(self):
        self.map.center_on(50.46683, 30.63908)
    
    def goto(self):
        self.map.center_on(49.836911, 24.037531)

class Main(App):
    def build(self):
        Builder.load_file("layout.kv")
        return MapViewExample()

Main().run()
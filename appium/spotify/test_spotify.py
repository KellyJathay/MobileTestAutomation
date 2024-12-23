
import time
import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSpotify(unittest.TestCase):
    
	@classmethod
	def setUpClass(cls):
		options = AppiumOptions()
		options.load_capabilities({
			"platformName": "Android",
			"appium:automationName": "uiautomator2",
			"appium:appPackage": "com.spotify.music",
			"appium:appActivity": "com.spotify.music.SpotifyMainActivity",
			"appium:fullReset": False,
			"appium:noReset": True
		})
		cls.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

	
	def test_new_playlist(self):
		driver = self.driver

		menu_your_library = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sua Biblioteca")
		menu_your_library.click()
		icon_plus = driver.find_element(by=AppiumBy.ID, value="com.spotify.music:id/button_create")
		icon_plus.click()
		select_playlist = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Playlist\")")
		select_playlist.click()
		btn_create = driver.find_element(by=AppiumBy.ID, value="com.spotify.music:id/continue_button")
		btn_create.click()
		container = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((AppiumBy.ID, "com.spotify.music:id/content_container"))
		) 
		container.click()
		
		icon_back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Voltar")
		icon_back.click()
		time.sleep(2)

	
	def test_edit_playlist(self):
		driver = self.driver

		menu_your_library = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sua Biblioteca")
		menu_your_library.click()
		item_library = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Minha playlist #1\")")
		item_library.click()
		icon_options = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(0)")
		icon_options.click()
		edit_playlist = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(3)")
		edit_playlist.click()
		edit_text = driver.find_element(by=AppiumBy.ID, value="com.spotify.music:id/title_edit_text")
		edit_text.clear()
		edit_text.send_keys("Teste")
	
		new_name = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.View\").instance(4)")
		new_name.click()
		btn_back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Voltar")
		btn_back.click()
		new_tem_library = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Teste\")")
		new_tem_library.click()
		library = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Teste\")")
		library.click()
		time.sleep(2)
		

	def test_add_artist(self):
		driver = self.driver

		menu_your_library = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sua Biblioteca")
		menu_your_library.click()
		btn_new_artist = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Adicionar artistas\")")
		btn_new_artist.click()
		search_field = driver.find_element(by=AppiumBy.ID, value="com.spotify.music:id/search_field_root")
		search_field.click()
		search = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Buscar\")")
		search.click()
		search.send_keys("Avicii")
		select_artist = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.spotify.music:id/labels\").instance(0)")
		select_artist.click()
		
		btn_done = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((AppiumBy.ID, "com.spotify.music:id/actionButton"))
		)
		btn_done.click()
		time.sleep(4)

	
	def test_play_and_pause_music(self):
		driver = self.driver

		menu_search = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Buscar")
		menu_search.click()
		search_music = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Busque alguma coisa pra ouvir")
		search_music.click()
		search = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"O que você quer ouvir?\")")
		search.click()
		search.send_keys("Dear Boy")
		
		click_song = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
		click_song.click()
		select_music = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Dear Boy\").instance(1)")
		select_music.click()
		btn_play = driver.find_element(by=AppiumBy.ID, value="com.spotify.music:id/button_play_and_pause")
		btn_play.click()		
		player_page = driver.find_element(by=AppiumBy.ID, value="com.spotify.music:id/track_info_view")
		player_page.click()
		btn_pause = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Pausar")
		btn_pause.click()
		time.sleep(3)

	@classmethod
	def tearDownClass(cls):
		if cls.driver:
			cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
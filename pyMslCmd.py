import pyxel
from enum import Enum,auto


WIDTH = 192
HEIGHT = 256    
FPS=30

class STATE(Enum):
    TITLE=0,
    PLAY=auto(),
    GAMEMENU=auto(),
    QUIT=auto()



#ゲームメインクラス        
class GameMain:

    #--------------------------------------------------------------------------------
    #Pyxelイニシャライズ
    #--------------------------------------------------------------------------------
    def __init__(self):
        self.GameState = STATE.TITLE

        self.QuitCount = 0

        pyxel.init(WIDTH, HEIGHT, title="PyMissleCommand",fps=FPS,quit_key=pyxel.KEY_NONE)
        #pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)


    def update(self):
        match self.GameState:
            case STATE.TITLE:
                self.update_title()
            case STATE.PLAY:
                print ("Play")
            case STATE.GAMEMENU:
                self.update_menu()
            case STATE.QUIT:
                self.update_quit()
            case _:
                print("default")




        #if pyxel.btnp(pyxel.KEY_Q):
        #    pyxel.quit()

    def draw(self):
            match self.GameState:
                case STATE.TITLE:
                     self.draw_title()
                case STATE.PLAY:
                    print ("Play")
                case STATE.GAMEMENU:
                    print ("GameMenu")
                    #self.draw_menu()
                case STATE.QUIT:
                    self.draw_quit()
                case _:
                    print("default")
#        pyxel.cls(0)
        #pyxel.text(10, 10, "Missle Command for Pyxel", pyxel.frame_count % 16)
        #pyxel.blt(61, 66, 0, 0, 0, 38, 16)
#        pyxel.line(0,0,WIDTH,HEIGHT,3)
    
    #--------------------------------------------------------------------------
    def update_title(self):
        #print(STATE.TITLE)

        if pyxel.btnp(pyxel.KEY_Q):
            self.QuitCount = 0
            self.GameState = STATE.QUIT
            pyxel.cls(0)

            #pyxel.quit()

    def draw_title(self):
        pyxel.cls(0)
        pyxel.text(10,10,"Missle Command",1)

        pyxel.text(10,16,"S:Game Start",7)
        pyxel.text(10,32,"Q:Quit",7)

    #--------------------------------------------------------------------------
    def update_menu(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.GameState = STATE.MENU

    def draw_menu(self):
        pyxel.cls(0)
        pyxel.text(10,10,"Mene",1)

    #--------------------------------------------------------------------------
    def update_quit(self):
        
        if self.QuitCount < FPS*2:
            self.QuitCount += 1
        else:
            pyxel.quit()

    def draw_quit(self):
            pyxel.text(0,0,"Thank you for playgame!",7)





GameMain()

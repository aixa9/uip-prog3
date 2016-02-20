class perro:
    pv=5
    pa=5

    def caminar(self):
        self.pv-=2
        self.pa+=1
    def correr(self):
        self.pv-=2
        self.pa+=1
    def dormir(self):
        self.pv+=1
        self.pa-=3
    def jugar (self):
        self.pa+=4
        self.pv-=1
    def comer (self):
        self.pv+=5
        self.pa+=1
    def imprimir(self):
        if self.pv == 0 and self.pa > 0:
            print ("pts de vida " + str(self.pv) + "\npts de alegria: " + str(self.pa))
            print ("SU PERRO MURIO FELIZ")
        elif self.pv > 0 or self.pa >= 0:
            print ("pts de vida " + str(self.pv) + "\npts de alegria: " + str(self.pa))
            print ("PERRO SIGUE CON VIDA")

lassie = perro()
lassie.dormir()
lassie.jugar()
lassie.comer()
lassie.jugar()
lassie.caminar()
lassie.dormir()
lassie.correr()
lassie.dormir()
lassie.comer()
lassie.imprimir()



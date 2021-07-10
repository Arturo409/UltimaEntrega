class Carro:
    def __init__(self, request):
        self.request=request
        self.session = request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro

    def agregar(self, producto):

        if(str(producto[0]) not in self.carro.keys()):
            self.carro[producto[0]]={
                "producto_id":producto[0],
                "descripcion":producto[1],
                "precio":producto[2],
                "cantidad":1,
                "imagen":producto[3],
            }
            
        else:
            for key, value in self.carro.items():
                #print (self.carro.items())
                
                if key==str(producto[0]):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"] = int(value["precio"]) + int(producto[2])
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto=str(producto)
        if producto in self.carro:
            del self.carro[producto]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto[0]):
                value["cantidad"] = value["cantidad"]-1
                value["precio"] = int(value["precio"]) - int(producto[2])
                if value["cantidad"]<1:
                    self.eliminar(producto[0])
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
data Disponibilidad = Libre | Ocupado deriving (Eq, Show)

lockers = [(100,(Ocupado,"ZD39I")),(101,(Libre,"JAH3I")),(103,(Libre,"IQSA9")),(105,(Libre,"QOTSA")),(109,(Ocupado,"893JJ")),(110,(Ocupado,"99292"))]


ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker k [] = []
ocuparLocker k (x:xs) | k == fst(x) && fst(snd(x)) == Libre = [(ocupar x)]++(xs)
                      | otherwise = [x]++(ocuparLocker k xs)     

ocupar :: Locker -> Locker
ocupar (ident,(dispo,ubi)) = (ident,(Ocupado,ubi))  
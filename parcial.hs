--1)
{-problema relacionesValidas (relaciones: seq⟨String x String⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) <=> relaciones no contiene ni tuplas repetidas, ni tuplas con ambas componentes iguales}
}-}
--A los fines de este problema consideraremos que dos tuplas son iguales si el par de elementos que las componen (sin importar el orden) son iguales. 

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True 
relacionesValidas (x:xs) | pertenece x xs = False 
                         | otherwise = relacionesValidas xs   

pertenece :: (String,String) -> [(String,String)] -> Bool
pertenece (k,y) [] = False 
pertenece (k,y) (x:xs) | (k,y) == x || (k,y) == reverso(x) = True
                       | otherwise = pertenece (k,y) xs 
 
reverso :: (String,String) -> (String,String)
reverso (x,y) = (y,x)

--2)
{-
problema personas (relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {res no tiene elementos repetidos}
  asegura: {res tiene exactamente los elementos que figuran en alguna tupla de relaciones, en cualquiera de sus posiciones}
} -}

personas :: [(String, String)] -> [String]
personas [] = []
personas (x:xs) | (pertenece2 (fst x) xs) && (pertenece2 (snd x) xs) = [] ++ personas xs
                | (pertenece2 (fst x) xs) = [snd x] ++ personas xs
                | (pertenece2 (snd x) xs) = [fst x] ++ personas xs
                | otherwise = [fst x] ++ [snd x] ++ personas xs   

pertenece2 :: String -> [(String,String)] -> Bool
pertenece2 k [] = False 
pertenece2 k (x:xs) | k == (fst x) || k == (snd x) = True
                    | otherwise = pertenece2 k xs 
 
--3)
{-problema amigosDe (persona: String, relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {res tiene exactamente los elementos que figuran en las tuplas de relaciones en las que una de sus componentes es persona}
} -}


amigosDe :: String -> [(String, String)] -> [String]
amigosDe k [] = [] 
amigosDe k (x:xs) | k == fst(x) = [snd x] ++ (amigosDe k xs)
                  | k == snd(x) = [fst x] ++ (amigosDe k xs)
                  | otherwise = [] ++ (amigosDe k xs)

--4)
{-
problema personaConMasAmigos (relaciones: seq⟨String x String⟩) : String {
  requiere: {relaciones no vacía}
  requiere: {relacionesValidas(relaciones)}
  asegura: {res es el Strings que aparece más veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}-}

-- personaConMasAmigos :: [(String, String)] -> String
-- personaConMasAmigos [x] = fst(x)
-- personaConMasAmigos (x:xs) | lenght(amigosDe(fst x)) > lenght(amigosDe(snd x)) = personaConMasAmigos()



-- lenght :: [String] -> Integer 
-- lenght [] = 0
-- lenght (x:xs) = 1 + lenght(xs) 

amigos :: [(String,String)] -> [String]
amigos [] = []
amigos (x:xs) = [fst x] ++ [snd x] ++ (amigos xs)

cantidadDeRep :: String -> [String] -> Integer 
cantidadDeRep k [] = 0   
cantidadDeRep k (x:xs) | k == x = 1 + (cantidadDeRep k xs)
                       | otherwise = (cantidadDeRep k xs)      

mayorCantidad :: [String] -> [String] -> String
mayorCantidad [x] _ = x 
mayorCantidad (x:y:xs) ys | (cantidadDeRep x ys) > (cantidadDeRep y ys) = mayorCantidad(x:xs) (ys)
                          | otherwise = mayorCantidad(y:xs) (ys)          

personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos (xs) = mayorCantidad (amigos xs) (amigos xs)
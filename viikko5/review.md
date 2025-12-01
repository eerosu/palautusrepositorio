Copilot teki neljä huomiota PR:sta. 

Näistä yksi oli hyvä huomio unohtuneista kovakoodatuista pelaajanimistä.

Kaksi oli pieniä huomioita [nitpick], jotka molemmat oli hyviä. Toinen oli hieman epämääräisesti nimetty apumetodi ja toinen oli turha ehtolause, koska pisteet eivät voi mennä negatiiviseksi.

Ensimmäinen ehdotettu muutos on mielestäni huonoin, koska Copilot haluaa varmistella raise ValueErrorilla tilannetta, jota ei mielestäni pääse syntymään eli toisella pelaajalla on 4 pistettä tai enemmän, mutta peli ei ole tasan. Ei tästä varmaankaan haittaa olisi, mutta mahdollisesti heikentäisi sisäistä laatua jälleen.

Tällaisessa pienessä koodimuutoksessa Copilotin katselmointi on mielestä enimmäkseen hyödyllinen, mutta esimerkiksi miniprojektia tehdessä se on ollut jopa haitallinen ja usein tekee asioista turhan monimutkaisia.





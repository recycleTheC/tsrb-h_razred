Toplina i termodinamika
=======================

.. admonition:: Autorova uputa za učenje

    **Učiti s razumijevanjem! :)**

    Koristiti više izvora za učenje: **vlastite bilješke, udžbenik...**

1. **Definicije temperature**

  **Temperatura je stanje zagrijanosti nekog tijela.**

  **Temperatura je mjera za srednju kinetičku energiju toplinskog gibanja čestica tijela.**

  :math:`\bar{E_k} \text~ T`

  *[čestice se gibaju nasumično, u svim smjerovima -> Brownovo gibanje]*


2. **Temperaturne ljestvice**

  1) Celziusova, **t/°C**
  2) termodinamička, **T/K** *(SI sustav)*
  3) Fahrenheitova, **t/°F**

  :math:`\Delta{t} = \Delta{T}` *[temperaturna razlika izražena u K ili °C prema iznosu je jednaka]*

  Pretvaranje: :math:`t/°F = \frac {9}{5} * t/°C + 32`

  .. image:: img/temp_ljestvice.png


3. **Zakoni linearnog i volumnog rastezanja**

.. admonition:: **Linearno rastezanje**

  .. image:: img/linearno_rastezanje.png

  |

  :math:`\beta` -> koeficijent linearnog rastezanja :math:`[K^-1][°C^-1]`

  :math:`\Delta{l}=l_0*\beta*\Delta{T}`

  :math:`l-l_0=l_0*\beta*\Delta{T}`

  :math:`l=l_0+l_0*\beta*\Delta{T}`

  :math:`l=l_0*(1+\beta*\Delta{t})`

.. admonition:: **Volumo rastezanje**

  .. image:: img/volumno_rastezanje.jpg

  |

  :math:`l^3=l_0^3*(1+\beta*\Delta{T})^3`

  :math:`V=V_0*(1+\beta*\Delta{T})^3`

  :math:`V=V_0*(1+\alpha*\Delta{T})`

  :math:`\Delta{V}=V_0*\alpha*\Delta{T}`

  :math:`\alpha=3*\beta`


4. **Definirati koeficijente linearnog i volumnog rastezanja**

  **Koeficijent linearnog rastezanja** je konstanta koja pokazuje za koji se dio
  početne duljine promjeni duljina tijela pri **promjeni temperature za 1K (1°C).**

  **Koeficijent volumnog rastezanja** je konstanta koja pokazuje za koji se dio
  početnog volumena promjeni volumen tijela pri **promjeni temperature za 1K (1°C).**

5. **Bimetalna traka**

  **Bimetalna traka** je traka napravljena od 2 međusobno spojene vrpce različitih metala.
  Pri određenoj temperaturi je bimetalna vrpca ravna. Pri zagrijavanju savija se na onu stranu
  na kojoj je metal manjeg koeficijenta linearnog rastezanja, a pri hlađenju obratno.

  .. image:: img/bimetalna_traka.png

6. **Anomalija vode**

  **Anomalija vode** je nepravilnost u promjeni obujma s temperaturom.

  Gustoća vode je najveća pri 4°C. Zbog anomalije, voda se počinje lediti od
  površine. Naime, u dodiru sa zrakom površinska se voda hladi i postaje gušća
  te se spušta, a na površinu dolazi toplija voda. To traje sve dok
  se površinska voda ne ohladi na 4°C. Hlađenjem površinske vode ispod 4°C, njezina
  gustoća postaje manja od gustoće toplije ispod nje. Zato voda s temperaturom nižom
  od 4°C ostaje na površini gdje će se daljnjim hlađenjem i zalediti.

  Zaleđivanje vode od površine prema dnu, a ne obratno, važno je za život flore i
  faune u rijekama, morima i jezerima.

  **Nepravilno toplinsko širenje nije svojstveno samo vodi, nego i mnogim drugim
  tekućinama.**

  .. image:: img/anomalija_vode.png

7. **Promjena gustoće s temperaturom; izvod jednadžbe**

  :math:`\rho=\frac  {m}{V}` ==> :math:`V=\frac  {m}{\rho}`

  :math:`V=V_0*(1+\alpha*\Delta{T})`

  :math:`\frac {m}{\rho}=\frac {m}{\rho_0}*(1+\alpha*\Delta{T})|:m`

  :math:`\frac {1}{\rho}=\frac {1+\alpha*\Delta{T}}{\rho_0}`

  .. admonition:: **Gustoća s promjenom temperature**

    :math:`\rho=\frac {\rho_0}{1+\alpha*\Delta{T}}`

8. **Boyle - Mariotteov zakon + jednadžbe**
  [**T=konst.** => **IZOTERMNA PROMJENA**]

  :math:`\frac {p_1*V_1}{T}=\frac {p_2*V_2}{T}|:T`

  .. admonition:: **Boyle - Mariotteov zakon**

    :math:`p_1*V_1=p_2*V_2`

    **Ako se plinu izotermno (uz stalnu temperaturu) promjeni stanje, tada je
    umnožak tlaka i obujma nakon promjene jednak umnošku tlaka i obujma prije promjene.**

  P ~ :math:`\frac {1}{V}`

  .. image:: img/boyle_mariotte.jpg
  *Jednostavan uređaj za opažanje izotermnih promjena stanja plina*

  .. image:: img/izotermna.png

|

  .. admonition:: **Izoterma**

    Linija (*hiperbola*) koja prikazuje ovisnost tlaka plina o volumenu plina pri konstantnoj
    temperaturi naziva se **izoterma**.


9. **Charlesov zakon + jednadžbe**
  [**V=konst.** => **IZOHORNA PROMJENA**]

  :math:`\frac {p_1*V}{T_1}=\frac {p_2*V}{T_2}|:V`

  .. admonition:: **Charlesov zakon**

    :math:`\frac {p_1}{T_1}=\frac {p_2}{T_2}`

    **Ako se plinu izhorno (uz stalni volumen) promjeni stanje, tada je
    kvocijent tlaka i termodinamičke temperature stalan.**

  p ~ T

  .. image:: img/izohorna1.png

|

  .. image:: img/izohorna2.png

|

  .. admonition:: **Izohora**

    Pravac koji prikazuje izohornu promjenu stanja plina naziva se **izohora**.

  .. image:: img/izohora.png


10. **Gay - Lussacov zakon + jednadžbe**

  [**p=konst.** => **IZOBARNA PROMJENA**]

  :math:`\frac {p_1*V_1}{T_1}=\frac {p_2*V_2}{T_2}|:p`

  .. admonition:: **Gay - Lussacov zakon**

    :math:`\frac {V_1}{T_1}=\frac {V_2}{T_2}`

    **Ako se plinu izobarno (uz stalni tlak) promjeni stanje, tada je
    kvocijent volumena i termodinamičke temperature stalan.**

  V ~ T

  .. image:: img/izobarna1.png
  *Ovisnot volumena plina o temperaturi uz konstantan tlak (V,T dijagram)*

  |

  .. image:: img/izobarna2.png
  *Ovisnot volumena plina o temperaturi uz konstantan tlak (V,t dijagram)*

  .. image:: img/izobare.png


11. **Kojim veličinama opisujemo stanje plina?**

  Stanje plina opisujemo **tlakom, volumenom i termodinamičkom temperaturom.**

12. Grafički prikaz izobarne, izohorne i izotermne promjene u koordinatnom sustavu

  .. image:: img/Picture1.png

  **Pogledati sve grafove u plinskim zakonima!**

13. **Zašto termodinamičku temperaturu zovemo apsolutnom?**

  Termodinamičku temperaturu nazivamo apsolutnom jer na temperaturi od 0 K
  (*apsolutna nula*) gotovo nema termičkoga gibanja čestica.

14. **Jednadžbe stanja idealnog plina**

  1) :math:`\frac {p*V}{T}=konst.`

     :math:`\frac {p_1*V_1}{T_1}=\frac {p_2*V_2}{T_2}|\text{krati se konstantna veličina}`

  |

  2) :math:`p*V=n*R*T`

     :math:`n` - **množina/količina tvari** [mol]

      :math:`n=\frac {m}{M}=\frac {N}{N_A}=\frac {V}{V_n}`

      :math:`N` - **broj čestica**

      :math:`N_A = 6,022*10^{23} mol^{-1}` - **Avogadrov broj**

      :math:`V_n` - **molarni volumen**

     :math:`R` - **opća plinska konstanta**

      :math:`R=8,314 \frac {J}{K*mol}`

  |

  3) :math:`p*V=\frac {N}{N_A}*R*T`

      :math:`k_B=\frac {R}{N_A}= 1,38*10^{-23} \frac {J}{K^{-1}}` - **Boltzmannova konstanta**

    :math:`p*V=N*k_B*T`


15. **Što je unutarnja energija? + jednadžbe**

  **Unutarnja energija** je zbroj kinetičkih energija toplinskih gibanja čestica
  i svih potencijalnih energija njihova međudjelovanja.

  :math:`\displaystyle{U=\sum_{i=1}^n E_{ki} + \sum_{i=1}^n E_{pi}}`

  :math:`U=\frac {3}{2}n*R*T`

  :math:`U=\frac {3}{2}p*V`


16. **Definicija topline**

  **Toplina** je dio unutarnje energije koja prelazi s jednog tijela na drugo zbog
  razlika u temperaturi.

  :math:`Q=m*c*\Delta{T}`

  :math:`c` - **specifični toplinski kapacitet**

17. **Specifični toplinski kapacitet i toplinski kapacitet**

  **Specifični toplinski kapacitet (c)** je veličina koja pokazuje koliku količinu topline
  izmjeni tijelo mase *1 kg* pri promjeni temperature za *1 K* (ili *1°C*).

    :math:`c=\frac {Q}{m(t_2-t_1)}`

  **Toplinski kapacitet (C)** je veličina koja pokazuje koliku količinu topline tijelo
  izmjeni pri promjeni temperature za *1 K* (ili *1°C*).

    :math:`C=c*m`

18. **Richmannovo pravilo smjese**

  Kada se dva tijela različitih temperatura stave u dodir ili pomiješaju, tijelo veće
  temperature predaje toplinu hladnijem sve do izjednačenja temperatura. Obilježimo li
  mase tijela s :math:`m_1` i :math:`m_2`, njihove specifične toplinske kapacitete s
  :math:`c_1` i :math:`c_2`, temperature prije dodira (miješanja) s :math:`t_1` i :math:`t_2`,
  a zajedničku temperaturu (temperaturu smjese) s :math:`\tau`, tada je toplina što je topije tijelo preda:

  :math:`Q_1=m_1*c_1(t_1-\tau)`

  a toplina što je hladnije tijelo primi:

  :math:`Q_2=m_2*c_2(\tau-t_2)`

  Ako su tijela izdvojena (izloirana) od drugih tijela, vrijedi: :math:`m_1*c_1(t_1-\tau)=m_2*c_2(\tau-t_2)`

  **Richmannovo pravilo** kaže da je količina topline koju tijelo niže temperature
  primi od tijela više temperature jednaka količini topline koju tijelo više
  temperature preda tijelu niže temperature.

19. **Opis kalorimetra**

  **Kalorimetar** je dobro izolirana posuda čije su stijenke ispunjene toplinskim
  izolatorom koji sprječava toplinsko vođenje, odnosno izmjenu topline sadržaja
  kalorimetra s okolinom. Najčešći izolator u stijenkama kalorimetra jest zrak.

  .. image:: img/kalorimetar.jpg

  *Kalorimetar na crtežu se razlikuje od kalorimetra korištenog na laboratorijskim vježbama!*

20. **Vrste agregatnih stanja i promjena agregatnih stanja**

  .. image:: img/agregacijska_stanja.jpg


21. **Promjena agregatnih stanja na primjeru: led-voda-vodena para**

  .. image:: img/promjena_stanja.jpg

  :math:`Q_{leda}=m*c_{led}*\Delta{T_1}`

  :math:`Q_t=m*\lambda`

  :math:`Q_{vode}=m*c_{vode}*\Delta{T_2}`

  :math:`Q_i=m*r`

  :math:`Q_{pare}=m*c_{pare}*\Delta{T_3}`

22. **Ovisnost temperature taljenja o visokom tlaku**

  Tvarima koje se pri taljenju *šire* temperatura taljenja raste s povećanjem
  vanjskog tlaka, dok se tvarima koje se pri taljenju *skupljaju (npr. led)*
  povećanjem vanjskog tlaka snižava temperatura taljenja.

  .. admonition:: Primjer: **Klizaljke i led**

     Led se pod klizaljkama (*visokim tlakom) rastali i pri nižoj temperaturi, a
     nastala se voda zaledi odmah nakon prolaska klizaljki.

     *[velika sila na malu površinu]

23. **Ovisnost temperature taljenja o čistoći tvari**

  Temperatura taljenja tvari snižava se dodavanjem primjesa.
  Talište legure je niže od temperature na kojoj se tali njezina komponenta s
  najnižim talištem.

24. **Latentna toplina taljenja i isparavanja**

  .. admonition:: **Latentna toplina taljenja**

    Latentna (specifična) toplina taljenja je količina topline koju mora primiti
    kilogram čvrste tvari da bi prešao u tekuće stanje na temperaturi taljenja.

    :math:`\lambda=\frac {Q_t}{m}` :math:`[\frac {J}{kg}]`

  .. admonition:: **Latentna toplina isparavanja**

    Latentna (specifična) toplina isparavanja je količina topline koju je potrebno
    utrošiti da bi kilogram tekućine prešao u paru na temperaturi vrenja.

    :math:`r=\frac {Q_i}{m}` :math:`[\frac {J}{kg}]`

25. **Talište / Vrelište**

  .. admonition:: **Talište**

    Talište (temperatura taljenja) je temperatura na kojoj tvar (**voda**) iz čvrstog agregacijskog
    stanja prelazi u tekuće agregacijsko stanje.


  .. admonition:: **Vrelište**

    Vrelište (temperatura vrenja) je temperatura na kojoj tvar (**voda**) iz tekućeg agregacijskog
    stanja prelazi u plinovito agregacijsko stanje.

26. **Ovisnost vrelišta o vanjskom tlaku**

  Temperatura vrenja ovisi o vanjskom tlaku na tekućinu.

  S povećanjem tlaka raste i vrelište tekućine. Snižavanjem tlaka snizuje se i
  vrelište tekućine. Iz tog razloga se na većim nadmorskim visinama (gdje je tlak
  niži) hrana u otvorenom loncu kuha sporije.

  .. admonition:: Primjer: **Ekspresni lonac**

    Voda pri normiranom atmorsferskom tlaku vrije na temperaturi 100°C i to je
    najviša temperatura što je voda može imati pri tom tlaku.
    U ekspresnom loncu, gdje je tlak nekoliko puta veći, voda vrije na temperaturi
    višoj od 100°C.


27. **Ovisnost vrelišta o čistoći tvari**

  Primjese dodane u tekućinu mogu povećati ili smanjiti temperaturu vrenja tekućine.

  .. admonition:: Primjer: **Dodavanje soli u vodu**

    Hrana se nešto brže kuha u slanoj vodi nego u čistoj. Dodatak soli povećava
    temperaturu vrenja vode.


28. **Kako računamo rad pri izobarnom/izotermnom/izohornom procesu?**

  1) izobarni proces: :math:`W=p*\Delta{V}`

  2) izotermni proces: :math:`W=n*R*T*\ln{\frac{p1}{p2}}`

  3) izohorni proces: :math:`W=0`

29. **Čime je grafički prikazan rad plina u p-V koordinatnom sustavu?**

  Rad plina je grafički prikazan površinom ispod grafa u p-V koordinatnom sustavu.

  .. image:: img/W_p-V.jpg


30. **Kako glasi I. zakon termodinamike?**

  .. admonition:: I. zakon termodinamike

    Količina topline koju plin primi jednaka je zbroju promjene unutarnje energije
    plina i rada što ga plin obavi.

    :math:`Q=W+\Delta{U}`

31. **Što je termodinamika?**

  Termodinamika je dio fizike u kojem istražujemo pretvorbu topline u mehanički rad.

32. **Što je termodinamički sustav?**

  Termodinamički sustav je bilo koji skup čestica u bilo kojem agregatnom stanju.

33. **Dogovoreni predznaci za ΔU, Q i W**

  +------------------------+----------------------------------+
  |      VRSTA PROCESA     | PROMJENA TERMODINAMIČKE VELIČINE |
  +                        +-----------+-----------+----------+
  |                        |     W     |     Q     |    ΔU    |
  +------------------------+-----------+-----------+----------+
  |  izotermna kompresija  |    < 0    |    < 0    |    = 0   |
  +------------------------+-----------+-----------+----------+
  |    izohorno hlađenje   |    = 0    |    < 0    |    < 0   |
  +------------------------+-----------+-----------+----------+
  |   izobarna ekspanzija  |    > 0    |    > 0    |    > 0   |
  +------------------------+-----------+-----------+----------+
  |  izotermna ekspanzija  |    > 0    |    > 0    |    = 0   |
  +------------------------+-----------+-----------+----------+
  |   izobarna kompresija  |    < 0    |    < 0    |    < 0   |
  +------------------------+-----------+-----------+----------+
  | adijabatska kompresija |    < 0    |    = 0    |    > 0   |
  +------------------------+-----------+-----------+----------+
  | adijabatska ekspanzija |    > 0    |    = 0    |    < 0   |
  +------------------------+-----------+-----------+----------+

34. **Adijabatski proces**

  .. admonition:: **Termodinamički procesi**

    Termodinamički proces je prijelaz termodinamičkog sustava iz jednog stanja
    u drugo.

  .. admonition:: **Adijabatski proces**

    **Adijabatski proces** je proces u kojem plin ne izmjenjuje toplinu s okolinom.

    Adijabatske procese (ekspanziju i kompresiju) prikazujemo u p-V koordinatnom
    sustavu. Graf nazivamo **adijabata**.

    .. image:: img/adijabatski_proces.jpg


35. **Kružni proces**

  Proces u kojem se plin vraća u početno stanje nazivmo **kružni proces**.

36. **Rad u kružnom procesu**


37. **Čime je predočen ukupni rad u kružnom procesu?**

  Rad je predočen **površinom** ispod grafa u **p-V koordinatnom sustavu**.

38. **Kada je ukupni rad pozitivan, kada negativan, a kada jednak nuli?**

  **W > 0** => rad plina je veći od rada vanjske sile (kružni proces teče u smjeru kazaljke na satu)

  **W < 0** => rad plina je manji od rada vanjske sile (kružni proces teče u smjeru suprotno od kazaljke na satu)

  **W = 0** => plin se iz stanja B vraća u početno stanje A istim putem kojim je iz stanja A došao u stanje B

  .. image:: img/kruzni_proces.jpg


39. **Obavljeni, uloženi i dobiveni rad**

  :math:`W_{obavljeni}` = rad koji obavi plin nad okolinom

  :math:`W_{uloženi}` = rad koji okolina obavi nad plinom

  :math:`W_{dobiveni}=W_{obavljeni}-W_{uloženi}`

40. **Što je toplinski stroj? (dijelovi)**

  **Toplinski stroj** je uređaj koji u kružnom procesu prevodi toplinu u mehnički rad.

  Tri su osnovna dijela svakog toplinskog stroja: **topliji** i **hladniji spremnik topline**
  te **radno sredstvo**.

  Radno sredstvo uzima toplinu (:math:`Q_1`) od toplijeg spremnika, dio te topline prevodi
  u mehanički rad (:math:`W`), a ostatak (:math:`Q_2`) predaje hladnijem spremniku.

  .. image:: img/toplinski_stroj.jpg

41. **Definiraj korisnost (djelotvornost) toplinskog stroja**

  **Djelotvornost (korisnost)** toplinskog stroja (:math:`\eta`) je omjer mehaničkog rada
  dobivenog u kružnom procesu i topline što ju je radno sredstvo primilo.

  :math:`\eta = \frac {W}{Q_1} = 1 - \frac {Q_2}{Q_1} = 1 - \frac {T_2}{T_1}`

42. Opiši rashladni stroj i toplinsku pumpu
43. **Opiši Carnotov kružni proces / nacrtati u p-V grafu**

  .. admonition:: **Analiza Carnotova kružnog procesa po fazama**

    .. image:: img/carnotov_kruzni_proces.png
    |
    :math:`1→2` **izotermna ekspanzija** – toplina :math:`Q_1` dovodi se plinu iz toplijeg spremnika pri stalnoj temperaturi :math:`T_1`.
    Nema promjene unutarnje energije plina, :math:`\Delta{U}=0`. Plin u cilindru obavlja rad koji je jednak dovedenoj
    toplini, zbog čega se klip podiže, a volumen plina povećava.

    :math:`W_{12}=Q_1`

    :math:`2→3` **adijabatska ekspanzija** – plin je termički izoliran pa nema izmjene topline s okolinom, odnosno :math:`Q=0`.
    Rad koji obavi plin jednak je smanjenu unutarnje energije pa se temperatura plina smanjuje na vrijednost
    :math:`T_2`. Klip se i dalje podiže, a volumen povećava.

    :math:`W_{23}=-\Delta{U}`

    :math:`3→4` **izotermna kompresija** – toplina :math:`Q_2` prenosi se hladnijem spremniku pri stalnoj temperaturi :math:`T_2`.
    Nema promjene unutarnje energije plina, odnosno :math:`\Delta{U}=0`.
    Na plinu se obavlja rad koji je prema prvom zakonu termodinamike po iznosu jednak otpuštenoj toplini :math:`Q_2`.
    Zbog obavljanja toga rada, klip se spušta, a volumen se plina u cilindru smanjuje.

    :math:`W_{34}=-Q_2`

    :math:`4→1` adijabatska kompresija – nema izmjene topline s okolinom, a rad koji se obavlja nad plinom
    jednak je povećanju unutarnje energije plina. Pritom plinu raste temperatura na vrijednost :math:`T_1`.
    Plin se vraća na početne vrijednosti tlaka i volumena i time se ciklus završava.

    :math:`W_{41}=\Delta{U}`

    .. image:: img/carnotov_kruzni_proces2.jpg
    |
    .. image:: img/carnotov_kruzni_proces3.jpg

44. **Kako glasi II. zakon termodinamike; perpetuum mobile I. i II. vrste**

  Perpetuum mobile I. vrste nije moguć jer se kosi sa zakonima termodinamike.

45. **Molekularno - kinetička teorija plinova / model idealnog plina**

  .. admonition:: **Molekularno - kinetička teorija plinova**

    :math:`v_{ef}=\sqrt{\frac {3*p*V}{m}}=\sqrt{\frac {3*R*T}{M}}`

    :math:`v_{ef} \text~ \sqrt{T}`

  .. admonition:: **Model idealnog plina**

    1. Čestice plina imaju kinetičku energiju, a potencijalnu energiju zanemarujemo.

      :math:`\displaystyle{U=\sum_{i=1}^n E_{ki}}`

    2. Plin je jako rijedak => volumen plina je zanemarivo manji od volumena posude.

    3. Sudari čestica plina su savršeno elastični.

    4. Vrijedi Newtonovska mehanika


46. **Što je idealni plin?** **[NEPROVJEREN SADRŽAJ]**

  Vrlo razrijeđeni plinovi ili plinovi kojima su molekule na vrlo velikim razmacima,
  ne sudaraju se, a pritom su i dimenzije samih molekula zanemarive u usporedbi s njihovim udaljenostima.
  Plin s takvim karakteristikama nazivamo idealni plin.

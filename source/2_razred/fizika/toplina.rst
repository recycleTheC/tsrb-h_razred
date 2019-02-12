Toplina i termodinamika
=======================

.. admonition:: Autorova uputa za učenje

    **Učiti s razumijevanjem! :)**
    
    Koristiti više izvora za učenje: **vlastite bilješke, udžbenik...**

1. **Definicije temperature**

  **Temperatura je stanje zagrijanosti nekog tijela.
  Temperatura je mjera za srednju kinetičku energiju toplinskog gibanja čestica tijela**

  :math:`\bar{E_k} \text~ T`

  *[čestice se gibaju nasumično, u svim svmjerovima -> Brownovo gibanje]*


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

  **Koeficijent linearnog rasteanja** je konstanta koja pokazuje za koji se dio
  početne duljine promjeni duljina tijela pri **promjeni temperature za 1K (1°C).**

  **Koeficijent volumnog rastezanja** je konstanta koja pokazuje za koji se dio
  početnog volumena promjeni volumen tijela pri **promjeni temperature za 1K (1°C).**

5. **Bimetalna traka**

  **Bimetalna traka** je traka napravljena od 2 međusobno spojne vrpce različitih metala.
  Pri određenoj temperaturi je bimetalna vrpca ravna. Pri zagrijavanju savija se na onu stranu
  na kojoj je metal manjeg koeficijenta linearnog rastezanja, a pri hlađenju obratno.

  .. image:: img/bimetalna_traka.png

6. **Anomalija vode**

  **Anomalija vode** je nepravilnost u promjeni obujma s temperaturom.

  Gustoća vode je najveća pri 4°C. Zbog anomalije, voda se počinje lediti od
  površine lediti od površine. Naime, u dodiru sa zrakom površinska se voda hladi
  i postaje gušća te se spušta, a na površinu dolazi toplija voda. To traje sve dok
  se površinska voda ne ohladi na 4°C. Hlađenjem površinske vode ispod 4°C, njezina
  gustoća postaje manja od gustoće toplije ispod nje. Zato voda s temperaturom nižom
  od 4°C ostaje na površini gdje će se daljnjim hlađenjem i zalediti.

  Zaleđivanje vode od površine prema dnu, a ne obratno, važno je za život flore i
  faune u rijekama, morima i jezerima.

  **Nepravilno toplinsko širenje nije svojstveno samo vodi, nego i mnogim drugim
  tekućinama.**

  .. image:: img/anomalija_vode.png

7. **Promjena gustoće s temperaturom; izvod jednadžbe**

  :math:`\rho=\frac  {m}{V}`

  :math:`V=\frac  {m}{\rho}`

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

    Linija (*hiperbola*) koji prikazuje ovisnost tlaka plina o volumenu plina pri konstantnoj
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

10. **Gay - Lussacov zakon + jednadžbe**
  [**p=konst.** => **IZOBARNA PROMJENA**]

  :math:`\frac {p_1*V}{T_1}=\frac {p_2*V}{T_2}|:p`

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


11. **Kojim veličinama opisujemo stanje plina?**

  Stanje plina opisujemo **tlakom, volumenom i termodinamičkom temperaturom.**

12. Grafički prikaz izobarne, izohorne i izotermne promjene u koordinatnom sustavu

    /

13. Zašto termodinamičku temperaturu zovemo apsolutnom?

  Termodinamičku temperatutu nazivamo apsolutnom jer na temperaturi od 0 K
  (*apsolutna nula*) gotovo nema termičkoga gibanja čestica.

14. Jednadžbe stanja idealnog toplina

  1) :math:`\frac {p*V}{T}=konst.`

     :math:`\frac {p_1*V_1}{T_1}=\frac {p_2*V_2}{T_1}|\text{krati se konstantna veličina}`

  |

  2) :math:`p*V=n*R*T`

     :math:`n` - **množina/količina tvari**

      :math:`n=\frac {m}{M}=\frac {N}{N_A}=\frac {V}{V_n}`

      :math:`N` - **broj čestica**

      :math:`N_A = 6,022*10^{23} mol^{-1}` - **Avogardov broj**

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

  **Specifični toplisnki kapacitet (c)** je veličina koja pokazuje koliku količinu topline
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
  a zajedničku temperaturu (temperaturu smjece) s :math:`\tau`, tada je toplina što je topije tijelo preda:

  :math:`Q_1=m_1*c_1(\tau-t_1)`

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


20. Vrste agregatnih stanja i promjena agregatnih stanja

  .. image:: img/agregacijska_stanja.jpg


21. Promjena agregatnih stanja na primjeru: led-voda-vodena para

  .. image:: img/promjena_stanja.jpg


22. Ovisnost temperature taljenja o visokom tlaku
23. Ovisnost temperature taljenja o čistoći tvari
24. Latentna toplina taljenja i isparavanja
25. Talište / Vrelište
26. Ovisnost vrelišta o vanjskom tlaku
27. Ovisnost vrelišta o čistoći tvari

28. Kako računamo rad pri izobarnom/izotermnom/izohornom procesu?
29. Čime je grafički prikazan rad plina u p-V koordinatnom sustavu?
30. Kako glasi I. zakon termodinamike?
31. Što je termodinamika?
32. Što je termodinamički sustav?
33. Dogovoreni predznaci za ΔU, Q i W
34. Adijabatski proces
35. Kružni proces
36. Rad u kružnom procesu
37. Čime je predočen ukupni rad u kružnom procesu?
38. Kada je ukupni rad pozitivan, kada negativan, a kada jednak nuli?
39. Obavljeni, uloženi i dobiveni rad
40. Što je toplinski stroj? (dijelovi)
41. Definiraj korisnost (djelotvornost) toplinskog stroja
42. Opiši rashladni stroj i toplinsku pumpu
43. Opiši Carnotov kružni proces / nacrtati u p-V grafu
44. Kako glasi II. zakon termodinamike; perpetuum mobile I. i II. vrste
45. Molekularno - kinetička teorija plinova / model idealnog plina
46. Što je idealni plin?

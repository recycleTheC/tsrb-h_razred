Magnetizam
==========

.. role:: red
.. role:: green
.. role:: blue
.. raw:: html

    <style>.red{color:red;}.blue{color:blue;}.green{color:green;}</style>

| `Elektrostatika <../elektrostatika/elektrostatika.html>`__
| `Elektromagnetizam <../elektromagnetizam/elektromagnetizam.html>`__

.. admonition:: Autorova uputa za učenje

    | **Učiti s razumijevanjem! :)**
    | Koristiti više izvora za učenje: **vlastite bilješke, udžbenik...**

.. contents:: Tablica sadržaja
  :local:
  :backlinks: none
  :depth: 3

.. admonition:: Konstante

  - apsolutna magnetska permeabilnost: :math:`\mu_0 = 4\pi * 10^{-7} \frac{Tm}{A}` 

1. Podjela magneta
^^^^^^^^^^^^^^^^^^
  +------------------+--------------------------------------+
  | Prirodni magneti | željezne rude (magnetit)             |
  +------------------+--------------------------------------+
  | Umjetni magneti  | permanentni (štapičasti, potkovasti) |
  |                  +--------------------------------------+
  |                  | elektromagneti                       |
  +------------------+--------------------------------------+

2. Koja je razlika između magneta i električnog naboja?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Magnet ima **stalno** magnetsko polje zbog konstantnog gibanja njegovih čestica, a električni naboj **stvara** magnetsko polje **kada se giba**.

3. Zemljino magnetsko polje
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Zemlja se ponaša kao veliki magnet. Uzrok Zemljina magnetskog polja je gibanje nabijenih čestica u njezinom tekućem dijelu.
  Južni pol Zemljinog magnetskog polja nalazi se u blizini Sjevernoga **geografskog** pola, a sjeverni magnetski pol je u blizini Južnoga **geografskog** pola.
  Položaj magnetskih polova pomaknut je u odnosu na položaje geografskih polova. 

  .. image:: zemljino_mag-polje.jpg
    :width: 50%
    :align: center

4. Oerstedov pokus i zaključci
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  .. image:: oerstedov1.jpg
  
  Postavi li se magnetna igla paralelno s vodičem kroz koji pustimo struju, igla se zakreće. Kad promijenimo smjer struje kroz vodič, magnetna igla se zakreće u suprotnom smjeru od prijašnjeg.

  Zaključak: **Električna struja oko vodiča stvara magnetsko polje**

5. O čemu ovisi magnetsko polje oko vodiča kojim teče električna struja (za ravni vodič, petlju i zavojnicu)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Ravni vodič

    | Magnetsko polje ravnog vodiča ovisi o udaljenosti od vodiča i jakosti struje kroz njega.
    | Obrtuno je proporcionalno udaljenosti od vodiča, proporcionalno je jakosti struje kroz vodič.

  .. admonition:: Petlja

    | Magnetsko polje petlje ovisi o polumjeru prstena i jakosti struje kroz njega. 
    | Obrtuno je proporcionalno polumjeru prstena, proporcionalno je jakosti struje kroz vodič.

  .. admonition:: Zavojnica

    | Magnetsko polje zavojnice ovisi o broju namotaja, jakosti struje kroz zavojnicu i duljini zavojnice. 
    | Obrtuno je proporcionalno duljini zavojnice, proporcionalno je jakosti struje kroz vodič i broju namotaja.

6. Kakve su silnice magnetskog polja?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Silnice magnetskog polja su **kružnog oblika**.

7. Što je to magnetska indukcija, kako se označava i mjerna jedinica?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Magnetska indukcija
  
    Magnetska indukcija (*ili gustoća magnetskog toka*) je vektorska veličina kojom opisujemo magnetsko polje, označava se slovom B, mjerna jedininca je tesla (T).

    | :math:`T = \frac{N}{Am}` 

8. Kako glase algebraski izrazi za magnetsku indukciju ravnog vodiča, petlje i zavojnice?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  .. admonition:: Ravni vodič

    :math:`B = \mu_0 \mu_r * \frac{I}{2 \pi r}`   

  .. admonition:: Petlja

    :math:`B = \mu_0 \mu_r * \frac{I}{2R}`   

  .. admonition:: Zavojnica
  
    :math:`B = \mu_0 \mu_r * \frac{N*I}{l}` 

9. Pravilo desne ruke za određivanje vektora B za ravni vodič
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Pravilo desne ruke: Ravni vodič

    Palac pokazuje smjer električne struje (I), a savijeni prsti desne ruke pokazuju smjer obilaženja silnica.

    .. image:: pdr_ravni.jpg
      :width: 50%
      :align: center
    

10. Što je to homogeno magnetsko polje i primjer za njega?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Homogeno magnetsko polje

    Homogeno magnetsko polje je magnetsko polje čiji je iznos i smjer magnetske indukcije u svakoj točki jednak.
    Silnice homogenog polja su međusobno paralelni pravci svuda jednake gustoće.

    Homogeno magnetsko polje -> magnetsko polje zavojnice

    .. image:: magnetsko_polje_zavojnice.jpg
  

11. Nacrtaj magnetske silnice za štapičasti magnet i potkovasti magnet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Štapičasti magnet

    .. image:: stapicasti_magnet.jpg
      :width: 50%
      :align: center
  
  .. admonition:: Potkovasti magnet

    .. image:: potkovasti_magnet.jpg
      :width: 50%
      :align: center

12. Što je i koliko iznosi apsolutna permeabilnost vakuuma, relativna permeabilnost?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Apsolutna permeabilnost vakuuma je konstanta magnetske permeabilnosti vakuuma, koja iznosi :math:`\mu_0 = 4\pi * 10^{-7} \frac{Tm}{A} [\frac{H}{m}]`.
  
  Relativna permeabilnost, :math:`\mu_r`, je fizikalna veličina s pomoću koje se opisuje utjecaj tvari na vanjsko magnetsko polje.​

13. Napišite jednadžbe za jakost magnetskog polja ravnog vodiča, petlje i zavojnice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  :math:`H = \frac{B}{\mu_0 \mu_r}` :math:`[\frac{A}{m}]`

  .. admonition:: Ravni vodič

    :math:`H = \frac{I}{2\pi r}`   

  .. admonition:: Petlja

    :math:`H = \frac{I}{2R}`   

  .. admonition:: Zavojnica
  
    :math:`H = \frac{N*I}{l}` 

14. Kako magnetsko polje djeluje na česticu u gibanju?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Magnetsko polje na česticu u gibanju djeluje Lorentzovom silom.

15. Kada je iznos magnetske sile na gibanje nabijene čestice u magnetskom polju najveći, a kada najmanji? (slika)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Iznos magnetske sile na gibanje nabijene čestice je najveći kada je kut (:math:`\alpha`) između vektora površine (:math:`\vec{S}`) i vektora magnetske indukcije (:math:`\vec{B}`) jednak 90°, a najmanji kada je jednak 0°. 

16. Pravilo desne ruke za magnetsku silu na naboj 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Pravilo desne ruke: smjer djelovanja Lorentzove sile

    Ispruženi prsti desne ruke pokazuju smjer magnetskih silnica, palac pokazuje smjer brzine. Smjer vektora sile kojom magnetsko polje djeluje na **pozitivno nabijenu česticu** okomito izlazi iz dlana.

    .. image:: pdr_lorentzovo.jpg
      :width: 50%
      :align: center

17. Algebraski izraz za Lorentzovu silu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Lorentzova sila

    :math:`\vec{F_L} = q * \vec{v} * \vec{B} * sin(\alpha)` 

    :math:`\alpha = \text{kut između } \vec{v} \text{ i } \vec{B}` 

18. Definirajte magnetski tok i navedite njegovu formulu s mjernom jedinicom
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Magnetski tok

    Magnetski tok je fizikalna veličina definirana umnoškom magnetske indukcije (:math:`B`) i površine (:math:`S`)
    kroz koju prolaze silnice magnetskog polja.

    :math:`\Phi = B * S * cos(\alpha)` :math:`[Wb]` 

    .. figure:: magnetski_tok.jpg
       :width: 50%
       :align: center

       :red:`Smjer` :math:`\vec{B}` je jednak :green:`smjeru vektora površine` :math:`\vec{S}`

    .. figure:: magnetski_tok2.jpg
      :width: 50%
      :align: center

      :red:`Smjer vektora površine` :math:`\vec{S}`, 
      :blue:`Smjer vektora magnetske indukcije` :math:`\vec{B}` 

    | :math:`\alpha = \text{kut između } \vec{S} \text{ i } \vec{B}` 

19. Amperova sila, formula, slika, pravilo desne ruke
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Amperova sila

    Amperova sila je sila kojom magnetsko polje djeluje na vodič kojim teče električna struja.

    :math:`F_{A} = B * I * l * sin(\alpha)` 

  .. admonition:: Pravilo desne ruke: Amperova sila

    .. image:: pdr_amper.jpg
      :width: 50%
      :align: center
    
    Ispruženi prsti desne ruke pokazuju smjer magnetske indukcije (B), palac pokazuje smjer struje. Smjer vektora sile kojom magnetsko polje djeluje na **vodič** okomito izlazi iz dlana.

    :math:`\alpha = \text{kut između } I*\vec{l} \text{ i } \vec{B}` 

20. Što je to elektromagnetska indukcija? Faradayev zakon indukcije za ravni vodič i zavojnicu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Elektromagnetska indukcija je induciranje napona magnetskim poljem.

  .. admonition:: Faradayev zakon indukcije za ravni vodič

    Inducirani elektromotorni napon proporcionalan je brzini promjene magnetskog toka, a djelovanjem se suprotstavlja uzroku indukcije.

    :math:`\epsilon_i = - \frac{\Delta\Phi}{\Delta t}`

  .. admonition:: Faradayev zakon indukiuje za zavojnicu
  
    U zavojnici s N namotaja, inducirani napon je N puta veći, odnos veličina vrijedi kao i za ravni vodič.

    :math:`\epsilon_i = - N * \frac{\Delta\Phi}{\Delta t}`

21. Flemingovo pravilo desne ruke za određivanje smjera induciranog napona: ako je palac u smjeru gibanja vodiča (v), kažiprst u smjeru polja (B), srednjak će pokazivati smjer induciranog napona, odnosno smjer kojim će teći struja ako je strujni krug zatvoren.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

22. Što može proizvesti promjenu jakosti magnetskog polja?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

23. Navedite slučajeve induciranja napona u zavojnici?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  - zavojnica miruje a kroz nju se pomiče magnet
  - magnet miruje a zavojnica se pomiče
  - unutar prve zavojnice se nalazi druga zavojnica kroz koju teče struja
    
    - zavjonica kroz koju teče struja -> primar (primarna zavojnica)
    
    - zavojnica u kojoj se inducira napon -> sekundar (sekundarna zavojnica)

24. Lenzovo pravilo
^^^^^^^^^^^^^^^^^^^^

  .. admonition:: Lenzovo pravilo
  
    Pravilo prema kojemu je smjer induciranog napona i struje u zavojnici kroz koju se mijenja magnetski tok uvijek takav da se suprotstavlja promjeni magnetskoga toka kojim je napon induciran.

    ili

    Suprotstavljanje induciranog napona uzroku indukcije.


25. Što se događa prilikom uključenja zavojnice u strujnom krugu? Zašto se u njoj inducira napon? Zašto vrijednost struje kroz nju ne poraste na najveću moguću vrijednost trenutno?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Prilikom uključenja zavojnice u strojni krug, na njenim krajevima se inducira napon koji se opire promjeni magnetskog toga kroz zavojnicu (koji na početku iznosi 0). 
  Jakost struje postepeno raste kako se smjanjuje promjena magnetskog toga u zavojnici.

26. Što se događa prilikom isključivanja zavojnice u krugu?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Na krajevima zavojnice se inducira napon.

27. Napišite jednadžbu koja povezuje magnetski tok i jakost struje kroz zavojnicu.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  :math:`I = \frac{\phi}{L}` 

28. Što je to induktivitet i o čemu ovisi?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

29. Kako računamo energiju magnetskog polja?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

30. Na kojem principu radi električni generator?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
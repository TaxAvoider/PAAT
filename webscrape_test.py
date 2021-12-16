from bs4 import BeautifulSoup as bs
import lxml.html
import requests
import urllib3

url = "https://www.wsj.com/market-data/quotes/company-list/sector/investing-securities"

# creating requests object
html = requests.get(url).content

# creating soup object
data = bs(html, 'html.parser')

# finding parent <ul> tag
parent = data.find("body").find("ul")

# finding all <li> tags
text = list(parent.descendants)

# printing the content in <li> tag
print(text)
for i in range(2, len(text), 2):
    print(text[i], end=" ")

""""
file = requests.get(url)

soup = bs(file.text, "lxml")

#print(html_data.prettify())
# data = html_data.find_all("thead")

# Below is the html I want, copied from the website, unsure how to get the data itself from the website
# html = ' <thead> <tr> <th>Name</th> <th>Country</th> <th>Exchange</th> </tr> </thead> <tbody> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ONCP"><span class="cl-name">141 Capital Inc.</span> (ONCP)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TURN"><span class="cl-name">180 Degree Capital Corp.</span> (TURN)</a></td> <td>United States</td> <td>XNAS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KEGS"><span class="cl-name">1812 Brewing Co. Inc.</span> (KEGS)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JM/XJAM/1834"><span class="cl-name">1834 Investments Ltd.</span> (1834)</a></td> <td>Jamaica</td> <td>XJAM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/EFSH"><span class="cl-name">1847 Holdings LLC</span> (EFSH)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CH/XSWX/HODL"><span class="cl-name">21Shares Crypto Basket Index ETP</span> (HODL)</a></td> <td>Switzerland</td> <td>XSWX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AU/XASX/TOT"><span class="cl-name">360 Capital REIT</span> (TOT)</a></td> <td>Australia</td> <td>XASX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TGOPF"><span class="cl-name">3i Group PLC</span> (TGOPF)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/III"><span class="cl-name">3i Group PLC</span> (III)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/DE/XFRA/IGQ5"><span class="cl-name">3i Group PLC</span> (IGQ5)</a></td> <td>Germany</td> <td>XFRA</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TGOPY"><span class="cl-name">3i Group PLC ADR</span> (TGOPY)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/FNINF"><span class="cl-name">49 North Resources Inc.</span> (FNINF)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CA/XTSX/FNR"><span class="cl-name">49 North Resources Inc.</span> (FNR)</a></td> <td>Canada</td> <td>XTSX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IT/XMIL/4AIM"><span class="cl-name">4AIM SICAF S.p.A.</span> (4AIM)</a></td> <td>Italy</td> <td>XMIL</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/HK/XHKG/2051"><span class="cl-name">51 Credit Card Inc.</span> (2051)</a></td> <td>Hong Kong</td> <td>XHKG</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/540776"><span class="cl-name">5Paisa Capital Ltd.</span> (540776)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/PK/XKAR/786"><span class="cl-name">786 Investment Ltd.</span> (786)</a></td> <td>Pakistan</td> <td>XKAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JFU"><span class="cl-name">9F Inc. ADR</span> (JFU)</a></td> <td>United States</td> <td>XNAS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CL/XSGO/CUPRUM"><span class="cl-name">A.F.P. Cuprum S.A.</span> (CUPRUM)</a></td> <td>Chile</td> <td>XSGO</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CL/XSGO/HABITAT"><span class="cl-name">A.F.P. Habitat S.A.</span> (HABITAT)</a></td> <td>Chile</td> <td>XSGO</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CL/XSGO/PROVIDA"><span class="cl-name">A.F.P. ProVida S.A.</span> (PROVIDA)</a></td> <td>Chile</td> <td>XSGO</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CA/XTSE/AGF.B"><span class="cl-name">A.G.F. Management Ltd. Cl B NV</span> (AGF.B)</a></td> <td>Canada</td> <td>XTSE</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AGFMF"><span class="cl-name">A.G.F. Management Ltd. Cl B NV</span> (AGFMF)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/530499"><span class="cl-name">A.K. Capital Services Ltd.</span> (530499)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AU/XASX/AYI"><span class="cl-name">A1 Investments &amp; Resources Ltd.</span> (AYI)</a></td> <td>Australia</td> <td>XASX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AU/XASX/A2B"><span class="cl-name">A2B Australia Ltd.</span> (A2B)</a></td> <td>Australia</td> <td>XASX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/0MG0"><span class="cl-name">Aareal Bank AG</span> (0MG0)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/XE/XETR/ARL"><span class="cl-name">Aareal Bank AG</span> (ARL)</a></td> <td>United States</td> <td>XETR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KW/XKUW/AAYAN"><span class="cl-name">Aayan Leasing &amp; Investment Co. K.S.C.</span> (AAYAN)</a></td> <td>Kuwait</td> <td>XKUW</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/LK/XCOL/AFSL.N0000"><span class="cl-name">Abans Finance PLC</span> (AFSL.N0000)</a></td> <td>Sri Lanka</td> <td>XCOL</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/FR/XPAR/ABCA"><span class="cl-name">ABC Arbitrage S.A.</span> (ABCA)</a></td> <td>France</td> <td>XPAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/0OPJ"><span class="cl-name">ABC Arbitrage S.A.</span> (0OPJ)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/SE/XNGM/ABIG"><span class="cl-name">Abelco Investment Group AB</span> (ABIG)</a></td> <td>Sweden</td> <td>XNGM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0013"><span class="cl-name">Abenlenda Inversiones S.A.</span> (S0013)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ACP.PRA"><span class="cl-name">Aberdeen Income Credit Strategies Fund 5.25% Perp. Pfd. Series A</span> (ACP.PRA)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/ASLI"><span class="cl-name">Aberdeen Standard European Logistics Income PLC</span> (ASLI)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/ASIZ"><span class="cl-name">Aberforth Split Level Income Trust PLC ZDP</span> (ASIZ)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/NO/XOSL/ABG"><span class="cl-name">ABG Sundal Collier Holding ASA</span> (ABG)</a></td> <td>Norway</td> <td>XOSL</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/0IZM"><span class="cl-name">ABG Sundal Collier Holding ASA</span> (0IZM)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ABGSF"><span class="cl-name">ABG Sundal Collier Holding ASA</span> (ABGSF)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/532057"><span class="cl-name">Abhinav Capital Services Ltd.</span> (532057)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/538952"><span class="cl-name">Abhinav Leasing &amp; Finance Ltd.</span> (538952)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/538935"><span class="cl-name">Abhishek Finlease Ltd.</span> (538935)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/511756"><span class="cl-name">Abirami Financial Services India Ltd.</span> (511756)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0015"><span class="cl-name">Abisal 72 S.A.</span> (S0015)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/PL/XWAR/AIN"><span class="cl-name">ABS Investment S.A.</span> (AIN)</a></td> <td>Poland</td> <td>XWAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AU/XASX/AEG"><span class="cl-name">Absolute Equity Performance Fund Ltd.</span> (AEG)</a></td> <td>Australia</td> <td>XASX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0019"><span class="cl-name">Abuvilla Inversiones S.A.</span> (S0019)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0023"><span class="cl-name">Acanto de Inversiones S.A.</span> (S0023)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/AC8"><span class="cl-name">Acceler8 Ventures PLC</span> (AC8)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CA/XTSE/ACD"><span class="cl-name">Accord Financial Corp.</span> (ACD)</a></td> <td>Canada</td> <td>XTSE</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S3404"><span class="cl-name">Acifiel S.A.</span> (S3404)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/539391"><span class="cl-name">Acme Resources Ltd.</span> (539391)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JP/XTKS/8572"><span class="cl-name">Acom Co. Ltd.</span> (8572)</a></td> <td>Japan</td> <td>XTKS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0030"><span class="cl-name">Aconcagua 6962 S.A.</span> (S0030)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S2274"><span class="cl-name">Actad Inversiones S.A.</span> (S2274)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0035"><span class="cl-name">Actimaaf Acciones Iberica S.A.</span> (S0035)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/511706"><span class="cl-name">Action Financial Services (India) Ltd.</span> (511706)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0036"><span class="cl-name">Activillo S.A.</span> (S0036)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0041"><span class="cl-name">Acueducto 2002 S.A.</span> (S0041)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0245"><span class="cl-name">Adaia Inversiones S.A.</span> (S0245)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/539506"><span class="cl-name">Adcon Capital Services Ltd.</span> (539506)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0045"><span class="cl-name">Addition S.A.</span> (S0045)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ADFT"><span class="cl-name">Adfitech Inc.</span> (ADFT)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/532056"><span class="cl-name">Adinath Exim Resources Ltd.</span> (532056)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ID/XIDX/ADMF"><span class="cl-name">Adira Dinamika Multi Finance</span> (ADMF)</a></td> <td>Indonesia</td> <td>XIDX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/540691"><span class="cl-name">Aditya Birla Capital Ltd.</span> (540691)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/532974"><span class="cl-name">Aditya Birla Money Ltd.</span> (532974)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/PL/XWAR/ADV"><span class="cl-name">Adiuvo Investments S.A.</span> (ADV)</a></td> <td>Poland</td> <td>XWAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S1302"><span class="cl-name">Adlergestion Inversiones S.A.</span> (S1302)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/511359"><span class="cl-name">Ad-Manum Finance Ltd.</span> (511359)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/FR/XPAR/ADV"><span class="cl-name">Advenis</span> (ADV)</a></td> <td>France</td> <td>XPAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/539773"><span class="cl-name">Advik Capital Ltd.</span> (539773)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ADYYF"><span class="cl-name">Adyen N.V.</span> (ADYYF)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/0YP5"><span class="cl-name">Adyen N.V.</span> (0YP5)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/NL/XAMS/ADYEN"><span class="cl-name">Adyen N.V.</span> (ADYEN)</a></td> <td>Netherlands</td> <td>XAMS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CH/XSWX/1N8"><span class="cl-name">Adyen N.V.</span> (1N8)</a></td> <td>Switzerland</td> <td>XSWX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/XE/XETR/1N8"><span class="cl-name">Adyen N.V.</span> (1N8)</a></td> <td>United States</td> <td>XETR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/MX/XMEX/ADYENN"><span class="cl-name">Adyen N.V.</span> (ADYENN)</a></td> <td>Mexico</td> <td>XMEX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ADYEY"><span class="cl-name">Adyen N.V. ADR</span> (ADYEY)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TH/XBKK/AEC"><span class="cl-name">AEC Securities PCL</span> (AEC)</a></td> <td>Thailand</td> <td>XBKK</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/HK/XHKG/900"><span class="cl-name">Aeon Credit Service (Asia) Co. Ltd.</span> (900)</a></td> <td>Hong Kong</td> <td>XHKG</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/MY/XKLS/5139"><span class="cl-name">AEON Credit Service (M) Bhd</span> (5139)</a></td> <td>Malaysia</td> <td>XKLS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JP/XTKS/8570"><span class="cl-name">Aeon Financial Service Co. Ltd.</span> (8570)</a></td> <td>Japan</td> <td>XTKS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TH/XBKK/AEONTS"><span class="cl-name">AEON Thana Sinsap (Thailand) PCL</span> (AEONTS)</a></td> <td>Thailand</td> <td>XBKK</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0800"><span class="cl-name">AF Dobra S.A.</span> (S0800)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AFCG"><span class="cl-name">AFC Gamma Inc.</span> (AFCG)</a></td> <td>United States</td> <td>XNAS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/0HAQ"><span class="cl-name">Affiliated Managers Group Inc.</span> (0HAQ)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AMG"><span class="cl-name">Affiliated Managers Group Inc.</span> (AMG)</a></td> <td>United States</td> <td>XNYS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/MGRB"><span class="cl-name">Affiliated Managers Group Inc. 4.75% Jr. Sub. Notes due 2060</span> (MGRB)</a></td> <td>United States</td> <td>XNYS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AATRL"><span class="cl-name">Affiliated Managers Group Inc. 5.15 Conv. Pfd.</span> (AATRL)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/MGR"><span class="cl-name">Affiliated Managers Group Inc. 5.875% Jr. Sub. Deb. due 2059</span> (MGR)</a></td> <td>United States</td> <td>XNYS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/PL/XWAR/AFH"><span class="cl-name">Aforti Holding S.A.</span> (AFH)</a></td> <td>Poland</td> <td>XWAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/CL/XSGO/AFPCAPITAL"><span class="cl-name">AFP Capital S.A.</span> (AFPCAPITAL)</a></td> <td>Chile</td> <td>XSGO</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/NG/XNSA/AFRIPRUD"><span class="cl-name">Africa Prudential Registrars PLC</span> (AFRIPRUD)</a></td> <td>Nigeria</td> <td>XNSA</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ZA/XJSE/ADW"><span class="cl-name">African Dawn Capital Ltd.</span> (ADW)</a></td> <td>South Africa</td> <td>XJSE</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ZA/XJSE/AEE"><span class="cl-name">African Equity Empowerment Investments Ltd.</span> (AEE)</a></td> <td>South Africa</td> <td>XJSE</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ZA/XJSE/AIL"><span class="cl-name">African Rainbow Capital Investments Ltd.</span> (AIL)</a></td> <td>South Africa</td> <td>XJSE</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ZA/XJSE/ATI"><span class="cl-name">Afristrat Investment Holdings Ltd.</span> (ATI)</a></td> <td>South Africa</td> <td>XJSE</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0053"><span class="cl-name">Agarus Inversiones S.A.</span> (S0053)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0060"><span class="cl-name">Agium Investium S.A.</span> (S0060)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/VN/XSTC/AGR"><span class="cl-name">Agribank Securities JSC</span> (AGR)</a></td> <td>Vietnam</td> <td>XSTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0066"><span class="cl-name">Aguilon de Gateruela y Vataros S.A.</span> (S0066)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JP/XTKS/7345"><span class="cl-name">Ai Partners Financial Inc.</span> (7345)</a></td> <td>Japan</td> <td>XTKS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/DE/XFRA/EBE"><span class="cl-name">aifinyo AG</span> (EBE)</a></td> <td>Germany</td> <td>XFRA</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JP/XTKS/8515"><span class="cl-name">Aiful Corp.</span> (8515)</a></td> <td>Japan</td> <td>XTKS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TH/XBKK/AIRA"><span class="cl-name">AIRA Capital PCL</span> (AIRA)</a></td> <td>Thailand</td> <td>XBKK</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/TH/XBKK/AF"><span class="cl-name">Aira Factoring PCL</span> (AF)</a></td> <td>Thailand</td> <td>XBKK</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JP/XTKS/8708"><span class="cl-name">Aizawa Securities Co. Ltd.</span> (8708)</a></td> <td>Japan</td> <td>XTKS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/AJB"><span class="cl-name">AJ Bell PLC</span> (AJB)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/511692"><span class="cl-name">Ajcon Global Services Ltd.</span> (511692)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KR/XKRX/027360"><span class="cl-name">Aju IB Investment Co. Ltd.</span> (027360)</a></td> <td>South Korea</td> <td>XKRX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/538778"><span class="cl-name">Akashdeep Metal Industries Ltd.</span> (538778)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JP/XTKS/8737"><span class="cl-name">Akatsuki Corp.</span> (8737)</a></td> <td>Japan</td> <td>XTKS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/HU/XBUD/AKKO"><span class="cl-name">AKKO Invest Nyrt.</span> (AKKO)</a></td> <td>Hungary</td> <td>XBUD</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0081"><span class="cl-name">Akorg Financiera S.A.</span> (S0081)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/OM/XMUS/AAIC"><span class="cl-name">Al Anwar Investments SAOG</span> (AAIC)</a></td> <td>Oman</td> <td>XMUS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/SA/XSAU/4130"><span class="cl-name">Al Baha for Investment &amp; Development Co.</span> (4130)</a></td> <td>Saudi Arabia</td> <td>XSAU</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JO/XAMM/BLAD"><span class="cl-name">Al Bilad for Securities &amp; Investment</span> (BLAD)</a></td> <td>Jordan</td> <td>XAMM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KW/XKUW/ALDEERA"><span class="cl-name">Al Deera Holding Co. K.P.S.C.</span> (ALDEERA)</a></td> <td>Kuwait</td> <td>XKUW</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/OM/XMUS/AMII"><span class="cl-name">Al Madina Investments Co. SAOG</span> (AMII)</a></td> <td>Oman</td> <td>XMUS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KW/XKUW/ALMANAR"><span class="cl-name">Al Manar Financing &amp; Leasing Co. KSCP</span> (ALMANAR)</a></td> <td>Kuwait</td> <td>XKUW</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AE/XADS/ALQUDRA"><span class="cl-name">Al Qudra Holding PJSC</span> (ALQUDRA)</a></td> <td>United Arab Emirates</td> <td>XADS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/AE/XDFM/ALRAMZ"><span class="cl-name">Al Ramz Corp. Investment &amp; Development Co.</span> (ALRAMZ)</a></td> <td>United Arab Emirates</td> <td>XDFM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KW/XKUW/ALSALAM"><span class="cl-name">Al Salam Group Holding Co. K.S.C.</span> (ALSALAM)</a></td> <td>Kuwait</td> <td>XKUW</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/OM/XMUS/SIHC"><span class="cl-name">Al Sharqiya Investment Holding Co. SAOG</span> (SIHC)</a></td> <td>Oman</td> <td>XMUS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/EG/NILX/ATLC"><span class="cl-name">Al Tawfeek Leasing Co.</span> (ATLC)</a></td> <td>Egypt</td> <td>NILX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/535916"><span class="cl-name">Alacrity Securities Ltd.</span> (535916)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/JO/XAMM/AMAL"><span class="cl-name">Al-Amal Financial Investments Co. PLC</span> (AMAL)</a></td> <td>Jordan</td> <td>XAMM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0919"><span class="cl-name">Alanje Inversiones S.A.</span> (S0919)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/ALNT"><span class="cl-name">Alantra Partners S.A.</span> (ALNT)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/UK/XLON/0OKB"><span class="cl-name">Alantra Partners S.A.</span> (0OKB)</a></td> <td>United Kingdom</td> <td>XLON</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0084"><span class="cl-name">Alava Inversiones S.A.</span> (S0084)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S1053"><span class="cl-name">Alcaravan Capital S.A.</span> (S1053)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S3122"><span class="cl-name">Alcestis Investment S.A.</span> (S3122)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0095"><span class="cl-name">Alcides Inversiones S.A.</span> (S0095)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0093"><span class="cl-name">Alco Inversiones Financieras S.A.</span> (S0093)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S2737"><span class="cl-name">Alcofam S.A.</span> (S2737)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0097"><span class="cl-name">Aldeu S.A.</span> (S0097)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0105"><span class="cl-name">Alekos Investments S.A.</span> (S0105)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/EG/NILX/ANFI"><span class="cl-name">Alexandria National Co. for Financial Investment</span> (ANFI)</a></td> <td>Egypt</td> <td>NILX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/FI/XHEL/ALEX"><span class="cl-name">Alexandria Pankkiiriliike Oyj</span> (ALEX)</a></td> <td>Finland</td> <td>XHEL</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/531156"><span class="cl-name">Alfavision Overseas (India) Ltd.</span> (531156)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ES/MABX/S0121"><span class="cl-name">Alianto Investment S.A.</span> (S0121)</a></td> <td>Spain</td> <td>MABX</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/ALMC"><span class="cl-name">Alimco Financial Corp.</span> (ALMC)</a></td> <td>United States</td> <td>OOTC</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/KW/XKUW/ALIMTIAZ"><span class="cl-name">Alimtiaz Investment Group K.S.C.</span> (ALIMTIAZ)</a></td> <td>Kuwait</td> <td>XKUW</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/IN/XBOM/532166"><span class="cl-name">Alka Securities Ltd.</span> (532166)</a></td> <td>India</td> <td>XBOM</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/PL/XWAR/ALG"><span class="cl-name">All In! Games S.A.</span> (ALG)</a></td> <td>Poland</td> <td>XWAR</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/NL/XAMS/ALLFG"><span class="cl-name">Allfunds Group PLC</span> (ALLFG)</a></td> <td>Netherlands</td> <td>XAMS</td> </tr> <tr> <td><a href="https://www.wsj.com/market-data/quotes/LK/XCOL/ALLI.N0000"><span class="cl-name">Alliance Finance Co. PLC</span> (ALLI.N0000)</a></td> <td>Sri Lanka</td> <td>XCOL</td> </tr> </tbody> '

# soup = bs(html, 'lxml')

# We're getting closer to what we want
table = soup.find_all('tr')
#items = soup.find("ul", class_="cl-tree cl-list")
#print(items)
#for li in items:
#    print(li)

data1 = soup.find('ul')
for li in data1.find_all("li"):
    print(li.text, end=" ")
"""

# print(items)
"""
row = [i.text for i in table]

asx_listed = []

for i in row:
    if "XASX" in i or "NSX" in i or "CHI-X" in i:
        asx_listed.append(i)

#print(asx_listed)

for i in asx_listed:
    ticker_split1 = i.split("(")
    ticker_split2 = ticker_split1[-1].split(")")
    title = ticker_split1[0]
    ticker = ticker_split2[0]
    exchange = (ticker_split2[-1].split())[-1]
"""
#    print(f"Name:{title:<80}Ticker: {ticker:<10} Exchange: {exchange:<10}")
#    print(f"{title:<80}{ticker:<10}{exchange:<10}")


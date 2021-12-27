# Labaratorinis #1

Užduoties tikslas: įvertinti kodonų ir dikodonų dažnio skirtumus žinduolių ir bakterijų virusuose.<br/>
Parašykite programą, kuri:  
1. Pateiktoje sekoje fasta formatu surastų visas start ir stop kodonų poras, tarp kurių nebūtų stop kodono (ir tiesioginei sekai ir jos reverse komplementui). 
2. Kiekvienam stop kodonui parinkti toliausiai nuo jo esanti start kodoną (su sąlyga, kad tarp jų nėra kito stop kodono)
3. Atfiltruokite visus fragmentus ("tai būtų baltymų koduojančios sekos"), kurie trumpesni nei 100 fragmentų.
4. Parašykite funkcijas, kurios įvertintų kodonų ir dikodonų dažnius (visi įmanomi kodonai/dikodonai ir jų atitinkamas dažnis  - gali būti nemažai nulių, jei jų sekoje nerasite).
5. Palyginkite kodonų bei dikodonų dažnius tarp visų sekų, atstumų matrica - kokią formulę naudosite?
6. Įvertinkite, ar bakteriniai ir žinduoliu virusai sudaro atskirus klasterius vertinant kodonų/dikodonų dažnių aspektu.

<h2>Ataskaita</h2>
Atstumų matricai apskaičiuoti naudojau euklidinio atstumo formulę. Kaip matome iš gautų kodonų ir dikodonų dažnių klasterizavimo medžių Neighbour Joining metodu (http://www.trex.uqam.ca/index.php?action=trex&menuD=1&method=2), dažnis tarp bakterijų ir žinduolių virusų skiriasi. Žinduolių virusai M4, M2, M1 ir bakterijų virusas B2 klasterizavosi į vieną grupę, bakterijų virusai B4, B1, B3 į kitą grupę. Labiausiai išsiskyrė žinduolių virusas M3 (Variola virusas).

# Labaratorinis #2

NC_045512.fasta 1 dalyje atsisiųstas nukleotidas iš NCBI.\
MN514967.1.fasta 2 dalyje atsisiųstas kupranugario virusas.\
completeSequence.fasta 2 dalyje gautas genomas.\
obtainedSequence.fasta 2 dalyje, sujungus NC_045512.fasta, MN514967.1.fasta ir completeSequence.fasta, gauta seka.\
(2e) Jei šio veiksmo neatliktume, paieškos rezultatuose gautuse įvairius Covid-19 viruso variantus.\
sortedSequence.fasta 3 dalyje surūšiuota seka.\
clusteredSequence.fasta 3 dalis po cluster.\
representativesSequence.fasta 3 dalis iš pradinio rinkinio išskirti id.\
D3W8N4.fasta 4 dalyje atsisiųstas proteinas.\
alignedSequences.fasta – 4 dalyje gauta seka po tblastn.\
translatedSequences.fasta – 4 dalyje gauta seka po translate.\
filteredSequences.fasta – 4 dalyje gauta seka po filtravimo.\
alignedMafftSequences.fasta – 4 dalyje gauta seka po lygiavimo.\
generatedTree.txt - 4 dalyje su fasttree sugeneruotas medis.\
main.ipynb – 5 dalies sprendimo kodas.

(6) Iš medžių galima pastebėti, kad Covid-19 virusas yra artimas šikšnosparnių ir pangolin koronavirusams, tačiau, ar giminingas camel virusui pasakyti negalime. Jei nebūtų naudojama išorinė grupė (out-group), interpretuojama būtų kitaip, giminystės ryšiai būtų kitaip atvaizduoti. Analizuojant Urbani SARS kilmę, galime pastebėti, kad jis labiau giminingas SARS viruso variantams nei šikšnosparnio ar kupranugario virusams. Ryškaus ryšio tarp šio ir Palm Civet nėra. Palm Civet kilmė matoma, jis giminingas šikšnosparnio virusui.

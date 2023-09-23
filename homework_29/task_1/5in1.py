# 5 tests from 1 to 100 workers, data=100
# you can Run and look diagrams, all data is ready


workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

list_value_1 = [50.9891152381897, 24.789255142211914, 16.138807773590088, 11.976574420928955, 9.737864017486572, 7.735967636108398, 6.86286473274231, 6.342570543289185, 5.736340045928955, 5.596058368682861, 5.181400775909424, 4.314876556396484, 3.673696279525757, 3.6342132091522217, 3.201716661453247, 3.2446513175964355, 2.961547613143921, 2.9140076637268066, 3.013061285018921, 3.0491230487823486, 2.361088275909424, 2.4395499229431152, 2.7729337215423584, 2.8066463470458984, 2.7433669567108154, 2.058016300201416, 2.115417718887329, 2.233137607574463, 2.077331781387329, 2.272554397583008, 2.71610951423645, 2.350478172302246, 2.9042561054229736, 1.5526151657104492, 1.5955226421356201, 1.7717714309692383, 1.6824896335601807, 1.630840539932251, 1.5961337089538574, 1.951399803161621, 1.7145028114318848, 1.7076854705810547, 1.8803551197052002, 1.9922242164611816, 1.8438518047332764, 3.4637961387634277, 1.9283688068389893, 1.8999032974243164, 2.4489619731903076, 2.1663894653320312, 1.6039917469024658, 1.0365805625915527, 1.3703749179840088, 1.0825107097625732, 1.1059997081756592, 1.1868081092834473, 1.0944664478302002, 1.806990146636963, 1.258164644241333, 1.7191379070281982, 1.679563283920288, 1.2553749084472656, 1.2747690677642822, 1.7605345249176025, 1.8128595352172852, 1.6927440166473389, 1.6898646354675293, 1.8303492069244385, 1.6998953819274902, 1.4324650764465332, 1.916172981262207, 1.8982841968536377, 1.4577457904815674, 1.5846197605133057, 3.0619633197784424, 1.837512493133545, 2.53072190284729, 1.835160493850708, 1.4543111324310303, 1.7244443893432617, 1.983243703842163, 1.8320074081420898, 1.8582067489624023, 2.0386970043182373, 2.132819652557373, 1.8402349948883057, 2.5299556255340576, 2.013054609298706, 2.657780885696411, 2.0907351970672607, 1.9400899410247803, 1.798579216003418, 2.0839855670928955, 2.053809404373169, 2.1870219707489014, 2.0305614471435547, 2.014420509338379, 2.0702617168426514, 2.181246280670166, 2.275481700897217]

list_value_2 = [44.72447180747986, 22.424553632736206, 15.4521324634552, 12.703092336654663, 9.139820575714111, 7.291640281677246, 6.38106369972229, 5.635722637176514, 5.312260150909424, 4.794830083847046, 4.403465509414673, 4.255474328994751, 3.8566086292266846, 3.6913962364196777, 3.3636081218719482, 3.0508008003234863, 3.2121410369873047, 3.40972638130188, 2.874966859817505, 2.848515510559082, 2.3153536319732666, 2.181835412979126, 2.552536964416504, 2.5232057571411133, 2.4788050651550293, 1.7699339389801025, 1.7651796340942383, 2.12994122505188, 2.224957227706909, 1.8936376571655273, 1.9857289791107178, 2.891244888305664, 2.142643451690674, 1.640824556350708, 1.654283046722412, 1.4579870700836182, 2.0602126121520996, 1.590360164642334, 2.734034299850464, 1.6865108013153076, 1.6610338687896729, 1.8848848342895508, 1.7651371955871582, 2.5243101119995117, 16.952673196792603, 2.9316580295562744, 2.4679923057556152, 2.1887128353118896, 2.7114129066467285, 2.0027167797088623, 1.603973388671875, 1.333538293838501, 1.137425422668457, 1.1245810985565186, 1.3124732971191406, 1.2762320041656494, 1.7540414333343506, 1.385514497756958, 1.139695405960083, 1.177872657775879, 1.8392024040222168, 1.716447114944458, 1.7018005847930908, 1.7261474132537842, 1.248046875, 1.290722131729126, 1.680950403213501, 1.3804852962493896, 1.5662729740142822, 1.9400005340576172, 2.559264659881592, 1.3906538486480713, 1.7810585498809814, 1.8506059646606445, 1.7012553215026855, 1.7095329761505127, 1.7255661487579346, 1.8028159141540527, 2.0916621685028076, 1.938826560974121, 2.472529649734497, 1.8132665157318115, 1.9725894927978516, 1.5317163467407227, 1.8550736904144287, 2.057730197906494, 2.055516242980957, 1.8379004001617432, 2.1121935844421387, 1.9982950687408447, 2.282701015472412, 1.822413682937622, 1.9001450538635254, 2.014141798019409, 1.9832324981689453, 2.217909336090088, 2.1164724826812744, 1.8929855823516846, 1.955063819885254, 2.177387237548828]

list_value_3 = [42.027161598205566, 23.59028434753418, 14.671802282333374, 11.789182424545288, 9.277937650680542, 7.2046568393707275, 6.897482872009277, 5.613605976104736, 5.297304153442383, 4.826719522476196, 4.391664028167725, 4.044032573699951, 3.72800874710083, 3.7544963359832764, 3.2569494247436523, 3.4743025302886963, 2.8752968311309814, 2.826690435409546, 3.002722978591919, 3.0352625846862793, 2.554931640625, 2.413403272628784, 2.5988712310791016, 2.4065194129943848, 2.4550015926361084, 1.8650546073913574, 2.2294185161590576, 2.3479321002960205, 2.0082316398620605, 2.051884889602661, 2.2063605785369873, 2.358567237854004, 3.059042453765869, 2.0558605194091797, 2.339510917663574, 1.6044363975524902, 1.7562317848205566, 1.7793200016021729, 1.6237878799438477, 8.970760583877563, 1.5635488033294678, 1.9721009731292725, 1.9340026378631592, 1.763437032699585, 1.822568655014038, 2.463829755783081, 19.66785502433777, 1.8682732582092285, 3.2415919303894043, 2.232517957687378, 0.9776191711425781, 1.021207332611084, 1.7696967124938965, 1.0806148052215576, 1.298421859741211, 1.5422918796539307, 1.33040452003479, 1.4462432861328125, 1.4090867042541504, 1.2534146308898926, 1.218867301940918, 1.7112977504730225, 1.190664291381836, 1.442756175994873, 1.4439349174499512, 1.1758770942687988, 1.7372100353240967, 1.6128652095794678, 1.861795425415039, 1.5535500049591064, 1.9427711963653564, 1.4231927394866943, 1.5471718311309814, 1.3788042068481445, 1.525977373123169, 1.6562788486480713, 1.7614359855651855, 2.0052132606506348, 1.884303092956543, 1.3759114742279053, 1.931800365447998, 1.9828243255615234, 1.5248029232025146, 1.870542287826538, 1.994616985321045, 2.206353187561035, 1.596400499343872, 3.160287857055664, 2.2293405532836914, 2.0203235149383545, 2.1261894702911377, 2.8402323722839355, 1.8790102005004883, 2.573577404022217, 1.9621877670288086, 2.031036138534546, 2.423668146133423, 4.3693647384643555, 2.7423384189605713, 3.164395332336426]

list_value_4 = [44.19031381607056, 21.517086505889893, 14.606607437133789, 10.992144107818604, 8.865875005722046, 7.249393463134766, 6.18143105506897, 5.385149002075195, 5.3546061515808105, 4.625419855117798, 4.066662788391113, 4.317659854888916, 4.472138404846191, 3.7548892498016357, 3.058380603790283, 3.26436185836792, 2.660085439682007, 2.840242385864258, 2.7665798664093018, 3.13786244392395, 2.91180419921875, 2.628678560256958, 2.923907518386841, 2.912705421447754, 3.744055986404419, 1.9001126289367676, 2.0007615089416504, 2.0611324310302734, 2.3100876808166504, 2.283669948577881, 2.3153483867645264, 2.8268117904663086, 2.7490079402923584, 1.7752685546875, 1.5251555442810059, 1.9085631370544434, 1.5800304412841797, 1.665773868560791, 1.9379909038543701, 1.6428046226501465, 1.7603957653045654, 1.9109282493591309, 2.084566116333008, 2.1908516883850098, 1.9633924961090088, 2.3336918354034424, 2.5352463722229004, 2.392608404159546, 2.4965274333953857, 2.4168429374694824, 1.220813274383545, 1.1922564506530762, 1.6288561820983887, 1.8070271015167236, 1.6703875064849854, 1.4273653030395508, 1.480236530303955, 1.1229712963104248, 1.8026347160339355, 1.5853757858276367, 1.3633334636688232, 1.2980785369873047, 1.1983590126037598, 1.2883574962615967, 1.8651759624481201, 2.43790602684021, 1.287712574005127, 1.713578462600708, 1.4801862239837646, 1.2404096126556396, 1.5182514190673828, 1.6977779865264893, 1.7745325565338135, 1.319504737854004, 1.6743452548980713, 1.427670955657959, 1.6192233562469482, 1.8902790546417236, 1.8490846157073975, 1.6327896118164062, 2.4105265140533447, 1.9418916702270508, 1.930659532546997, 1.776526927947998, 1.779289960861206, 2.014954090118408, 2.086198091506958, 2.7298245429992676, 2.0536677837371826, 1.888366937637329, 1.8571224212646484, 2.116896629333496, 2.0056333541870117, 1.9815659523010254, 1.836549997329712, 2.2601723670959473, 2.838318109512329, 5.649696350097656, 1.9151935577392578, 2.680572509765625]

list_value_5 = [43.25003147125244, 20.906063318252563, 14.525252342224121, 10.847426891326904, 9.022750854492188, 7.021415948867798, 7.027913570404053, 5.473256587982178, 5.15803337097168, 4.867631673812866, 4.4955408573150635, 3.997009515762329, 3.595177173614502, 3.6588144302368164, 3.2394871711730957, 3.6078779697418213, 2.762010335922241, 2.8444225788116455, 2.8088538646698, 2.9352564811706543, 2.3265926837921143, 2.940742254257202, 3.1189961433410645, 2.6365861892700195, 3.3771092891693115, 2.0714914798736572, 1.9258408546447754, 2.4726264476776123, 2.6643621921539307, 2.9485111236572266, 4.3491129875183105, 2.9535021781921387, 2.590766191482544, 1.95914888381958, 1.7124109268188477, 1.5920348167419434, 1.7061166763305664, 1.8717281818389893, 1.581589698791504, 2.1750361919403076, 2.2726516723632812, 1.9326717853546143, 1.7138304710388184, 1.9324250221252441, 1.9266769886016846, 2.166015148162842, 2.2741270065307617, 2.019890785217285, 2.0917181968688965, 1.9430973529815674, 2.573617935180664, 1.5425519943237305, 1.402085781097412, 1.0593936443328857, 1.1780712604522705, 1.4990947246551514, 1.5478768348693848, 2.097867012023926, 1.1400220394134521, 1.1504580974578857, 1.978766918182373, 1.298527479171753, 1.2682485580444336, 1.2551589012145996, 1.5860462188720703, 1.2334115505218506, 1.974259614944458, 2.107466459274292, 2.1726343631744385, 2.755401849746704, 2.304733991622925, 1.758885383605957, 1.656125545501709, 2.0589160919189453, 2.240213632583618, 1.879992961883545, 2.3938167095184326, 2.332867383956909, 2.112027168273926, 1.8660666942596436, 1.9640822410583496, 2.0552148818969727, 1.8892719745635986, 1.902700424194336, 3.1553080081939697, 2.7394049167633057, 2.365351676940918, 2.1330349445343018, 1.9329683780670166, 2.1309330463409424, 2.177781820297241, 2.795102596282959, 3.4620368480682373, 2.301921844482422, 2.3366453647613525, 2.1502139568328857, 2.115980625152588, 4.080436944961548, 2.370762825012207, 2.4269585609436035]

list_value_average = []
for i in range(100):
    add = round(((list_value_1[i]+list_value_2[i]+list_value_3[i]+list_value_4[i]+list_value_5[i]) / 5), ndigits=3)

    list_value_average.append(add)


import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Scatter(x=workers[30:100],
                     y=list_value_average[30:100], mode='lines+markers')],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()

import subprocess
import sys
import os
import classify


def flow(inpdb):
    with open(inpdb) as ts:
        with open('subgraph.txt', 'w') as outxt:
            p = subprocess.Popen("../P1", stdin=ts, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            q = subprocess.Popen(
                ('grep', 'Code'), stdin=p.stdout, stdout=outxt)

    (stdoutput, erroutput) = q.communicate()

    predict = classify.clas()

    mapping = {
        'Argo': ['4n41.dat', '4n47.dat', '4w5o.dat', '4z4c.dat', '4z4d.dat', '4z4f.dat', '5awh.dat', '5g5s.dat', '5g5t.dat', '5i4a.dat', '5js1.dat', '5ki6.dat', '5t7b.dat', '5ux0.dat'],
        'E2F': ['2IW6.dat', '2IW8.dat', '2R7G.dat', '2UUE.dat', '2UZB.dat', '2UZD.dat', '2UZE.dat', '2UZL.dat', '2V22.dat'],
        'Globin': ['1HBG.dat', '1JF3.dat', '1JF4.dat', '1JL6.dat', '1JL7.dat', '1VRE.dat', '1VRF.dat', '2HBG.dat'],
        'HSP': ['1P5Q.dat', '1Q1C.dat', '1QZ2.dat', '1ROT.dat', '1ROU.dat', '4DRJ.dat', '4LAV.dat', '4LAW.dat', '4LAX.dat', '4LAY.dat'],
        'Histone': ['5b31.dat', '5b32.dat', '5b33.dat', '5bt1.dat', '5ix1.dat', '5ix2.dat', '5kgf.dat', '5kr7.dat', '5nl0.dat'],
        'bcl-2': ['2ABO.dat', '3BL2.dat', '3DVU.dat'],
        'bcl_xl': ['1AF3.dat', '1BXL.dat', '1G5J.dat', '1LXL.dat', '1MAZ.dat', '1PQ0.dat', '1PQ1.dat', '1R2D.dat', '1R2E.dat', '1R2G.dat''1R2H.dat', '1R2I.dat', '1YSG.dat', '1YSI.dat', '1YSN.dat', '2B48.dat', '2BZW.dat', '2O1Y.dat', '2PON.dat'],
        'pkd': ['2yrl.dat', '4aqo.dat', '4jrw.dat', '4xed.dat', '5ezd.dat'],
        'serine': ['1KY9.dat', '1LCY.dat', '1SOT.dat', '1SOZ.dat', '1TE0.dat', '1VCW.dat', '1Y8T.dat', '2PZD.dat', '2R3Y.dat', '2Z9I.dat', '2ZLE.dat', '3CS0.dat'],
        'serpin': ['1ANT.dat', '1ATH.dat', '1DB2.dat', '1JMJ.dat', '1JVQ.dat', '1LK6.dat', '1OVA.dat', '1R1L.dat', '1SEK.dat', '2ZNH.dat', '3EVJ.dat']
    }
    truth = ''
    for key in mapping:
        if os.path.basename(inpdb) in mapping[key]:
            truth = key

    os.remove('subgraph.txt')
    return predict, truth


if __name__ == '__main__':
    print(flow(sys.argv[1]))

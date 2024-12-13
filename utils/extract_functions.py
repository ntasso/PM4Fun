def extract_data_PM4Silt(g_o,phases,x,y):
    data = {'q':[],'p':[],
            'sx':[],'sy':[],'sz':[],'sxy':[],'ea':[],'eps_v':[],'gamxy':[],'gams':[],
            'eps_1':[],'eps_2':[],'eps_3':[],'eps_xx':[],'eps_yy':[],'phase':[],'s1':[],'s2':[],'s3':[],
            'suratio':[],'su':[],'rumax':[],'pmin':[],'zmax':[],'Cs':[],'M':[],'Gamma':[],
            'pcs':[],'xi':[],'e':[],'Mcurrent':[],'K':[],'G':[],'alphastatic':[],'Kc':[],
            'K0':[],'sigmav0':[],'ru':[],'ruextreme':[],'gmax/2extreme':[],'BCI':[],
            'g/2max':[],'Md':[],'Mb':[],'D':[],'alphaxx':[],'alphayy':[],'alphaxy':[],
            'rulimit':[],'lpr':[],'txyratio':[],'txyratioextreme':[]}
    phaseid=-1
    for phase in phases:
        phaseid +=1
        for step in phase.Steps:
            try:
                data['suratio'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[0],(x,y)))
                data['su'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[1],(x,y)))
                data['rumax'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[2],(x,y)))
                data['pmin'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[3],(x,y)))
                data['zmax'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[4],(x,y)))
                data['Cs'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[5],(x,y)))
                data['M'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[6],(x,y)))
                data['Gamma'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[7],(x,y)))
                data['pcs'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[8],(x,y)))
                data['xi'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[9],(x,y)))
                data['e'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[10],(x,y)))

                data['Mcurrent'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[11],(x,y)))
                data['K'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[12],(x,y)))
                data['G'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[13],(x,y)))
                data['alphastatic'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[14],(x,y)))
                data['Kc'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[15],(x,y)))
                data['K0'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[16],(x,y)))
                data['sigmav0'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[17],(x,y)))
                data['ru'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[18],(x,y)))

                data['ruextreme'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[19],(x,y)))
                data['gmax/2extreme'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[20],(x,y)))
                data['BCI'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[21],(x,y)))
                data['g/2max'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[22],(x,y)))
                data['Md'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[23],(x,y)))
                data['Mb'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[24],(x,y)))
                data['D'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[25],(x,y)))

                data['alphaxx'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[26],(x,y)))
                data['alphayy'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[27],(x,y)))
                data['alphaxy'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[28],(x,y)))
                data['rulimit'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[29],(x,y)))
                data['lpr'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[30],(x,y)))
                data['txyratio'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[31],(x,y)))
                data['txyratioextreme'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.StateParameters[32],(x,y)))

  

                data['q'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.DeviatoricStress,(x,y)))
                data['p'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.MeanEffStress,(x,y))*-1)
                data['sx'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.SigxxE,(x,y))*-1)
                data['sy'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.SigyyE,(x,y))*-1)
                data['sz'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.SigzzE,(x,y))*-1)
                data['s1'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.SigmaEffective1,(x,y))*-1)
                data['s2'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.SigmaEffective2,(x,y))*-1)
                data['s3'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.SigmaEffective3,(x,y))*-1)
                data['sxy'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Sigxy,(x,y))*-1)
                data['ea'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Eps1,(x,y))*-100)
                data['eps_v'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.TotalVolumetricStrain,(x,y))*100)
                data['eps_1'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Eps1,(x,y))*-1)
                data['gamxy'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.PGamxy,(x,y))*-1)
                data['gams'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.PhaseDeviatoricStrain,(x,y))*-1)
                data['eps_2'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Eps2,(x,y))*-1)
                data['eps_3'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Eps2,(x,y))*-1)
                data['eps_xx'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Epsxx,(x,y))*-1)
                data['eps_yy'].append(g_o.getsingleresult(step,g_o.ResultTypes.Soil.Epsyy,(x,y))*-1)
                data['phase'].append(phaseid)
            except:
                print('a step was not extracted')
                continue


    return data

def extract_params_PM4Silt(g_i,mat_idx):
    params = {}
    params['Suratio'] = g_i.Materials[mat_idx].User1.value
    params['Su'] = g_i.Materials[mat_idx].User2.value
    params['G0'] = g_i.Materials[mat_idx].User3.value
    params['hp0'] = g_i.Materials[mat_idx].User4.value
    params['patm'] = g_i.Materials[mat_idx].User5.value
    params['ng'] = g_i.Materials[mat_idx].User6.value
    params['h0'] = g_i.Materials[mat_idx].User7.value
    params['e0'] = g_i.Materials[mat_idx].User8.value
    params['lambda'] = g_i.Materials[mat_idx].User9.value
    params['phicv'] = g_i.Materials[mat_idx].User10.value
    params['nbwet'] = g_i.Materials[mat_idx].User11.value
    params['nbdry'] = g_i.Materials[mat_idx].User12.value
    params['nd'] = g_i.Materials[mat_idx].User13.value
    params['Ad0'] = g_i.Materials[mat_idx].User14.value
    params['rumax'] = g_i.Materials[mat_idx].User15.value
    params['zmax'] = g_i.Materials[mat_idx].User16.value
    params['cz'] = g_i.Materials[mat_idx].User17.value
    params['Ceps'] = g_i.Materials[mat_idx].User18.value
    params['CGD'] = g_i.Materials[mat_idx].User19.value
    params['ckaf'] = g_i.Materials[mat_idx].User20.value
    params['nu'] = g_i.Materials[mat_idx].User21.value
    params['CGconsol'] = g_i.Materials[mat_idx].User23.value
    params['FSu'] = g_i.Materials[mat_idx].User24.value
    params['psiR'] = g_i.Materials[mat_idx].User25.value
    params['dR'] = g_i.Materials[mat_idx].User26.value
    params['phic'] = g_i.Materials[mat_idx].User27.value
    params['cc'] = g_i.Materials[mat_idx].User28.value

    return params

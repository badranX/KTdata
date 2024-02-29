import yamld



meta = yamld.read_metadata('./assist2009.yaml')

problem2KCs = meta['problem2KCs']
n_kc = meta['n_kc']

def generate_correlated_kc(kcs):
    kcs1 = map(lambda x: x + n_kc, kcs)
    kcs2 = map(lambda x: x + 2*n_kc, kcs)
    return kcs + list(kcs1) +  list(kcs2)

l = map(generate_correlated_kc, problem2KCs)

l = list(l)

df = yamld.read_dataframe('./assist2009.yaml')

df.attrs['problem2KCs'] = l
df.attrs['n_kc'] = n_kc*3

yamld.write_dataframe('./corr_assist2009.yaml', df)



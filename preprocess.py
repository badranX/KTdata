import yamld

n_dub = 1

meta = yamld.read_metadata('./assist2009.yaml')

problem2KCs = meta['problem2KCs']
n_kc = meta['n_kc']
avg_kc_per_exer = meta['avg_kc_per_exer']

def generate_correlated_kc(kcs):
    new = list(kcs)
    for i in range(1, n_dub+1):
        kcs1 = list(map(lambda x: x + i*n_kc, kcs))
        new.extend(kcs1)

    return new
l = map(generate_correlated_kc, problem2KCs)

l = list(l)

df = yamld.read_dataframe('./assist2009.yaml')

df.attrs['problem2KCs'] = l
df.attrs['n_kc'] = n_kc*(n_dub + 1)
df.attrs['avg_kc_per_exer'] = avg_kc_per_exer*(n_dub + 1)

yamld.write_dataframe('./corr_assist2009.yaml', df)



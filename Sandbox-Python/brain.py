import brainstem

if __name__ == '__main__':
    spec = brainstem.discover.findFirstModule(brainstem.link.Spec.USB)
    print(spec) 

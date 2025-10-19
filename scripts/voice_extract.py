from extract_features import extract_mfcc

if __name__ == "__main__":
    pessoas_falando = "data/pessoas_falando.wav"
    features = extract_mfcc(pessoas_falando)
    if features is not None:
        print("MFCC extraídos com sucesso:")
        print(features)
    else:
        print("Falha na extração dos MFCCs.")

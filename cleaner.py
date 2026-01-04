import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
 
    df = df.drop_duplicates()

    
    df.columns = [c.strip() for c in df.columns]

  
    for col in df.columns:
        if df[col].dtype == "object":
           
            s = df[col].astype(str).str.replace(",", "", regex=False).str.strip()
           
            numeric = pd.to_numeric(s, errors="coerce")
            if numeric.notna().mean() > 0.7:
                df[col] = numeric

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("Unknown")

    return df

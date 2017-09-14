def cigar_party(cigars, is_weekend):
  if (cigars < 40):
    return False
  if (is_weekend == False):
    if (cigars >= 40 and cigars <= 60):
      return True
    if (cigars < 40 or cigars > 60):
      return False
  if (is_weekend):
    if (cigars >= 40):
      return True
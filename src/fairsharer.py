def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Args:
        values (list): 1D array of values.
        num_iterations (int): Integer to set the number of iterations.
        share (float): Fraction to distribute (default 0.1).

    Returns:
        list: Updated values after iterations.
    """
    # Defensive Copy: Wir arbeiten auf einer Kopie, um die Originaldaten nicht zu verfälschen
    values_new = list(values)

    for _ in range(num_iterations):
        # 1. Höchsten Wert finden
        max_val = max(values_new)
        max_idx = values_new.index(max_val)

        # 2. Verteilungsmenge berechnen
        distribution = max_val * share

        # 3. Werte aktualisieren
        # Hauptwert reduzieren
        values_new[max_idx] -= 2 * distribution

        # Linker Nachbar (Index -1 ist in Python automatisch das letzte Element -> Kreis geschlossen)
        values_new[max_idx - 1] += distribution

        # Rechter Nachbar (Modulo-Operator sorgt für Kreisschluss am Ende der Liste)
        right_idx = (max_idx + 1) % len(values_new)
        values_new[right_idx] += distribution

    return values_new
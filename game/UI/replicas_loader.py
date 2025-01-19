import pygame


class ReplicasLoader:
    def __init__(self, load_file: str):
        self.replicas: list[tuple[str, list[str]]] = []
        with open(load_file, 'r') as file:
            lines = file.readlines()
        current_replica_speaker = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if not line.startswith('Replica '):
                self.replicas[-1][1].append(line)
                continue
            current_replica_speaker = line[len('Replica '):]  # Skip replica title
            self.replicas.append((current_replica_speaker, []))

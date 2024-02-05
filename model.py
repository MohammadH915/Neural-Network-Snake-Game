import torch
import torch.nn as nn

class QNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim).double()  # Update data type to double
        self.fc2 = nn.Linear(hidden_dim, hidden_dim).double()
        self.fc3 = nn.Linear(hidden_dim, hidden_dim).double()
        self.fc4 = nn.Linear(hidden_dim, output_dim).double()
        self.relu = nn.ReLU()

    def forward(self, x):
        l1 = self.relu(self.fc1(x.double()))  # Ensure input data type is double
        l2 = self.relu(self.fc2(l1))
        l3 = self.relu(self.fc3(l2))
        l4 = self.fc4(l3)
        return l4

def get_network_input(player, apple):
    proximity = player.get_proximity()
    x = torch.cat([
        torch.from_numpy(player.pos).float(),
        torch.from_numpy(apple.pos).float(),
        torch.from_numpy(player.dir).float(),
        torch.tensor(proximity).float()
    ])
    return x
from django.contrib import admin
from .models import Post
from .models import Equipamento
from .models import Cidade
from .models import Uf
from .models import Pais
from .models import Fornecedor
from .models import Material
from .models import Pagamento
from .models import Setor
from .models import Tarefa
from .models import Funcionario
from .models import Obra


admin.site.register(Post)
admin.site.register(Equipamento)
admin.site.register(Cidade)
admin.site.register(Uf)
admin.site.register(Pais)
admin.site.register(Fornecedor)
admin.site.register(Material)
admin.site.register(Pagamento)
admin.site.register(Setor)
admin.site.register(Tarefa)
admin.site.register(Funcionario)
admin.site.register(Obra)

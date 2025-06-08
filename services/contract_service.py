from dao.contract_dao import ContractDAO

class ContractService:
    """Фасад для валідації контрактів постачальників."""
    def __init__(self, contract_dao: ContractDAO):
        self.contract_dao = contract_dao

    def validate_contract(self, contract_id: int):
        """Може перевіряти, чи контракт містить усю необхідну контактну інформацію."""
        contract = self.contract_dao.find_by_id(contract_id)
        # Тут може бути додаткова логіка
        return contract is not None and contract.contact_info != ""

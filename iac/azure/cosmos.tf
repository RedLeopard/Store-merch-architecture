// Terraform stub — SAFE: does not create resources until you add real values.
//
// 1) Copy this to a throwaway trial project/subscription.
// 2) Set budgets/alerts first. 3) `terraform plan` only. 4) Delete trial when done.
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = ">= 3.0" }
    google  = { source = "hashicorp/google",  version = ">= 5.0" }
  }
}

// TODO: add azurerm_cosmosdb_account (COMMENTED)
class AddFingerprintToUserFiles < ActiveRecord::Migration
  def change
  	add_column :user_files, :attachment_fingerprint, :string
  end
end
